import pandas as pd
import random
import string
import json
import os

# 生成随机字符串的函数
def random_string(length=10):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

# 生成假数据的函数，只修改case_name, description, content_body
def generate_fake_data_with_fixed_fields(num_records, project_id, fixed_record):
    fake_data = []
    for i in range(1, num_records + 1):
        case_name = f"test_success_case{i:02d}"
        description = f"这是登录功能的第{i}个测试用例"
        # 生成随机的用户名和密码
        username = random_string(8)
        password = random_string(10)
        # 构造内容主体
        content_body = json.dumps({
            "username_or_email": username,
            "password": password
        })
        # 将生成的数据添加到列表中，其他字段使用固定记录的值
        fake_data.append({
            "case_name": case_name,
            "description": description,
            "content_if_id": fixed_record['content_if_id'],
            "content_if_name": fixed_record['content_if_name'],
            "content_header": fixed_record['content_header'],
            "content_body": content_body,
            "content_extract": fixed_record['content_extract'],
            "project_id": project_id
        })
    return fake_data

# 读取上传的Excel文件
file_path = './excels/test_login.xlsx'  # 请确保文件路径正确
if not os.path.exists(file_path):
    raise FileNotFoundError(f"文件 {file_path} 不存在，请检查文件路径。")

# 尝试读取上传的Excel文件的第一个工作表
try:
    df = pd.read_excel(file_path, sheet_name=0)
except Exception as e:
    raise ValueError(f"读取文件时出错: {str(e)}")

# 获取原始数据中的不变字段值
original_record = df.iloc[0]
original_content_if_id = original_record['content_if_id']
original_content_if_name = original_record['content_if_name']
original_content_header = original_record['content_header']
original_content_extract = original_record['content_extract']
original_project_id = original_record['project_id']

# 生成30条假数据
fake_data = generate_fake_data_with_fixed_fields(30, original_project_id, original_record)

# 创建一个新的Excel写入对象，使用openpyxl引擎
fake_data_file_path = file_path.rsplit('.', 1)[0] + '_fakedata.xlsx'
with pd.ExcelWriter(fake_data_file_path, engine='openpyxl') as writer:
    # 直接在第一个sheet中添加假数据
    df_combined = pd.concat([df, pd.DataFrame(fake_data)], ignore_index=True)
    df_combined.to_excel(writer, sheet_name='Sheet1', index=False)


print(f'新文件的完整路径是{fake_data_file_path}，数据生成完成，请检查文件')