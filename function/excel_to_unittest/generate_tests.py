
import argparse
import pandas as pd
from pathlib import Path

def generate_test_file(sheet_name, df, output_dir: Path):
    test_file_name = f"test_{sheet_name.replace('/', '_')}.py"
    test_file_path = output_dir / test_file_name

    # 更新列名校验
    required_columns = ['test_title', 'test_method', 'url', 'test_data', 'request_json', 'status']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Excel sheet {sheet_name} 缺少必需列：{required_columns}")

    with open(test_file_path, 'w', encoding='utf-8') as f:
        f.write("import requests\nimport unittest\n\n")
        f.write(f"class Test{sheet_name.replace('/', '_')}(unittest.TestCase):\n")

        for index, row in df.iterrows():
            test_title = row['test_title']
            test_method = row['test_method'].lower()  # 转换为小写，方便比较
            url = row['url']
            test_data = row['test_data']
            request_json = row['request_json']
            status = row['status']

            f.write(f"    def test_{test_title.replace(' ', '_')}(self):\n")
            if test_method == 'get':
                f.write(f"        response = requests.get('{url}', params={test_data})\n")
            elif test_method == 'post':
                f.write(f"        response = requests.post('{url}', json={test_data})\n")
            else:
                f.write(f"        raise ValueError(f'不支持的请求方法: {{test_method}}')\n")

            f.write(f"        self.assertEqual(response.status_code, {status})\n")
            f.write(f"        self.assertEqual(response.json(), {request_json})\n\n")

        f.write("if __name__ == '__main__':\n")
        f.write("    unittest.main()\n")

def scan_excel_files(excel_dir: Path, output_dir: Path):
    # 创建输出目录（包括父目录）
    output_dir.mkdir(parents=True, exist_ok=True)

    # 使用Path.glob遍历Excel文件
    for file_path in excel_dir.glob("*.xls*"):
        try:
            excel_file = pd.ExcelFile(file_path)
            for sheet_name in excel_file.sheet_names:
                df = excel_file.parse(sheet_name)
                generate_test_file(sheet_name, df, output_dir)
        except Exception as e:
            print(f"处理文件 {file_path.name} 时出错: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Generate tests from Excel files')
    parser.add_argument('--excel-dir',
                       default='Exceldata',
                       type=Path,
                       help='Excel文件目录路径 (默认: %(default)s)')
    parser.add_argument('--output-dir',
                       default='testplatform/tests/unit',
                       type=Path,
                       help='测试用例输出目录 (默认: %(default)s)')
    args = parser.parse_args()

    try:
        scan_excel_files(args.excel_dir, args.output_dir)
        print(f"成功生成测试用例到目录: {args.output_dir.resolve()}")
    except Exception as e:
        print(f"生成测试用例失败: {str(e)}")

if __name__ == "__main__":
    main()
