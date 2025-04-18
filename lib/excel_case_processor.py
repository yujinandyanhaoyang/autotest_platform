import os
import time
import pandas as pd
from base.models import Case, Project, Interface
import json


class ExcelCaseProcessor:
    def __init__(self, temp_file_path, settings):
        self.temp_file_path = temp_file_path
        self.settings = settings
        self.valid_cases = []

    def check_file_format(self):
        required_fields = [
            'case_name', 'description', 'content_if_id',
            'content_if_name', 'content_header', 'content_body',
            'content_extract', 'project_id'
        ]

        try:
            xl = pd.ExcelFile(self.temp_file_path)
            sheet_names = xl.sheet_names
            all_valid = True

            for sheet_name in sheet_names:
                df = xl.parse(sheet_name)

                # 检查第一行是否包含所有必需字段
                if not all(field in df.columns for field in required_fields):
                    all_valid = False
                    continue

                for index, row in df.iterrows():
                    try:
                        # 检查 content_if_id 和 project_id 是否存在于数据库中
                        content_if_id = row['content_if_id']
                        project_id = row['project_id']

                        Interface.objects.get(if_id=content_if_id)
                        project = Project.objects.get(prj_id=project_id)
                        # print(f'content_if_id的检查结果：{Interface.objects.get(if_id=content_if_id)}')
                        # print(f'project__id的检查结果：{Project.objects.get(prj_id=project_id)}')


                        content = {
                            'content_if_id': content_if_id,
                            'content_if_name': row['content_if_name'],
                            'content_header': row['content_header'],
                            'content_body': json.loads(row['content_body']),
                            'content_extract': row['content_extract']
                        }
                        print(f'content的检查结果：{content}')
                        case_data = {
                            'case_name': row['case_name'],
                            'description': row['description'],
                            'project': project,
                            'content': json.dumps(content)
                        }
                        print(f'case_data的检查结果：{case_data}')
                        self.valid_cases.append(case_data)
                    except (Interface.DoesNotExist, Project.DoesNotExist):
                        continue

            return all_valid and bool(self.valid_cases)
        except Exception as e:
            print(f"处理文件时出错: {e}")
            return False

    def save_cases_to_db(self):
        if self.valid_cases:
            cases_to_create = [Case(**case) for case in self.valid_cases]
            Case.objects.bulk_create(cases_to_create)

    def move_file_to_destination(self, file_name):
        from datetime import datetime
        now = datetime.now()
        year = str(now.year)[2:]
        month = str(now.month).zfill(2)

        # 构建目标保存路径
        save_dir = os.path.join('resource', 'data', 'excel', year, month)
        if not os.path.exists(save_dir):
            os.makedirs(save_dir, exist_ok=True)
        final_file_path = os.path.join(save_dir, file_name)

        # 移动文件到目标目录
        os.rename(self.temp_file_path, final_file_path)

    def delete_temp_file(self, max_retries=3, delay=1):
        retries = 0
        while retries < max_retries:
            try:
                if os.path.exists(self.temp_file_path):
                    os.remove(self.temp_file_path)
                break
            except PermissionError:
                retries += 1
                time.sleep(delay)
        if retries == max_retries:
            print(f"无法删除文件 {self.temp_file_path}，达到最大重试次数。")

