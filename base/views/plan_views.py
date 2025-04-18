from django.shortcuts import render
from base.models import Plan, Project, Environment, Report
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import time

from lib.execute import Execute

# 计划管理
def plan_index(request):
    plan_list = Plan.objects.all()
    return render(request, "base/plan/index.html", {"plan_list": plan_list})

# 计划添加
def plan_add(request):
    if request.method == 'POST':
        plan_name = request.POST['plan_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        env_id = request.POST['env_id']
        environment = Environment.objects.get(env_id=env_id)
        description = request.POST['description']
        content = request.POST.getlist("case_id")
        plan = Plan(plan_name=plan_name, project=project, environment=environment, description=description, content=content)
        plan.save()
        return HttpResponseRedirect("/base/plan/")
    prj_list = Project.objects.all()
    return render(request, "base/plan/add.html", {"prj_list": prj_list})

# 计划执行
def plan_run(request):
    if request.method == 'POST':
        #print("使用的是POST方法，开始向目标接口发送请求")
        plan_id = request.POST['plan_id']
        plan = Plan.objects.get(plan_id=plan_id)
        env_id = plan.environment.env_id
        case_id_list = eval(plan.content)
        case_num = len(case_id_list)
        content = []
        pass_num = 0
        fail_num = 0
        error_num = 0
        for case_id in case_id_list:
            execute = Execute(case_id, env_id)
            case_result = execute.run_case()
            print(f'执行结果是{case_result}')
            content.append(case_result)
            if case_result["result"] == "pass":
                pass_num += 1
            if case_result["result"] == "fail":
                fail_num += 1
            if case_result["result"] == "error":
                error_num += 1
        report_name = plan.plan_name + "-" + time.strftime("%Y%m%d%H%M%S")
        if Report.objects.filter(plan=plan):
            Report.objects.filter(plan=plan).update(report_name=report_name, content=content, case_num=case_num,
                                                    pass_num=pass_num, fail_num=fail_num, error_num=error_num)
        else:
            report = Report(plan=plan, report_name=report_name, content=content, case_num=case_num,
                            pass_num=pass_num, fail_num=fail_num, error_num=error_num)
            report.save()
        return HttpResponse(plan.plan_name + " 执行成功！")

# 计划删除
def plan_delete(request):
    print("同时设计多个组件的删除功能，暂时不做")

def plan_update(request):
    print("表单比较复杂，暂时不做")