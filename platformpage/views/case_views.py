import os

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from Autotest_platform import settings
from platformpage.models import Project, Case
from lib.excel_case_processor import  ExcelCaseProcessor
from lib.execute import Execute


def case_index(request):
    case_list = Case.objects.all()
    return render(request, "platformpage/case/index.html", {"case_list": case_list})

def case_add(request):
    if request.method == 'POST':
        case_name = request.POST['case_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        description = request.POST['description']
        content = request.POST['content']
        case = Case(case_name=case_name, project=project, description=description, content=content)
        case.save()
        return HttpResponseRedirect("/platformpage/case/")
    prj_list = Project.objects.all()
    return render(request, "platformpage/case/add.html", {"prj_list": prj_list})

def case_run(request):
    if request.method == 'POST':
        case_id = request.POST['case_id']
        env_id = request.POST['env_id']
        execute = Execute(case_id, env_id)
        case_result = execute.run_case()
        return JsonResponse(case_result)


def  case_update(request):
    print("目前不太重要，后续再补充")


def case_delete(request):
    if request.method == 'GET':
        case_id = request.GET['case_id']
        Case.objects.filter(case_id=case_id).delete()
        return HttpResponseRedirect("/platformpage/env/")


# 外部导入测试用例
def case_uplode(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            if not file.name.endswith(('.xlsx', '.xls')):
                return JsonResponse({'ret': 1, 'msg': '请上传 Excel 文件.'}, status=400)

            # 构建临时保存路径
            temp_dir = os.path.join(settings.BASE_DIR, 'temp')
            if not os.path.exists(temp_dir):
                os.makedirs(temp_dir, exist_ok=True)
            temp_file_path = os.path.join(temp_dir, file.name)

            try:
                # 保存文件到临时目录
                with open(temp_file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                # 初始化处理器
                processor = ExcelCaseProcessor(temp_file_path, settings)

                # 检查文件格式并收集有效用例
                is_valid = processor.check_file_format()
                # print(f'文件格式检查结果：{is_valid}')

                if is_valid:
                    # 保存用例到数据库
                    # print('开始将数据保存到数据库')
                    processor.save_cases_to_db()
                    # 移动文件到目标目录
                    # 权限问题，暂时不删除临时文件
                    # processor.move_file_to_destination(file.name)
                    return JsonResponse({'ret': 0, 'msg': '资源上传成功，测试用例已保存到数据库.'}, status=201)
                else:
                    # 处理失败，删除临时文件
                    # 权限问题，暂时不删除临时文件
                    # processor.delete_temp_file()
                    return JsonResponse({'ret': 1, 'msg': 'Excel 文件无效或存在脏数据，未保存.'}, status=400)
            except Exception as e:
                # 发生异常，删除临时文件
                # 权限问题，暂时不删除临时文件
                # processor = ExcelCaseProcessor(temp_file_path, settings)
                # processor.delete_temp_file()
                return JsonResponse({'ret': 1, 'msg': f'处理文件时出错: {str(e)}'}, status=500)
        else:
            return JsonResponse({'ret': 1, 'msg': '请上传文件.'}, status=400)
    else:
        return JsonResponse({'ret': 1, 'msg': '请使用 POST 方法上传文件.'}, status=405)








