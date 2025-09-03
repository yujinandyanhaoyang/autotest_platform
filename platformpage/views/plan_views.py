from django.shortcuts import render
from platformpage.models import Plan, Project, Environment, Report
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
import time
import os
from lib.execute import Execute

# 计划管理
def plan_index(request):
    plan_list = Plan.objects.all()
    return render(request, "platformpage/plan/index.html", {"plan_list": plan_list})

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
        return HttpResponseRedirect("/platformpage/plan/")
    prj_list = Project.objects.all()
    return render(request, "platformpage/plan/add.html", {"prj_list": prj_list})

# 计划执行
def plan_run(request):
    if request.method == 'POST':
        plan_id = request.POST['plan_id']
        plan = Plan.objects.get(plan_id=plan_id)
        # 获取环境 ID 并记录
        env_id = plan.environment.env_id
        # 解析用例 ID 列表并记录
        case_id_list = eval(plan.content)
        case_num = len(case_id_list)
        content = []
        pass_num = 0
        fail_num = 0
        error_num = 0

        # 执行用例并记录结果
        for case_id in case_id_list:
            execute = Execute(case_id, env_id)
            case_result = execute.run_case()
            # print(f'执行结果是{case_result}')
            content.append(case_result)
            if case_result["result"] == "pass":
                pass_num += 1
            if case_result["result"] == "fail":
                fail_num += 1
            if case_result["result"] == "error":
                error_num += 1
        return HttpResponse(plan.plan_name + " 执行成功！")

# 计划删除
def plan_delete(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        if plan_id:
            try:
                plan = Plan.objects.get(plan_id=plan_id)
                plan.delete()
            except Plan.DoesNotExist:
                pass
        return HttpResponseRedirect("/platformpage/plan/")
    return HttpResponseRedirect("/platformpage/plan/")

def plan_update(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan_id')
        if plan_id:
            try:
                plan = Plan.objects.get(plan_id=plan_id)
                plan.plan_name = request.POST['plan_name']
                plan.project_id = request.POST['prj_id']
                plan.environment_id = request.POST['env_id']
                plan.description = request.POST['description']
                plan.content = request.POST.getlist('case_id')
                plan.save()
            except Plan.DoesNotExist:
                pass
        return HttpResponseRedirect('/platformpage/plan/')
    else:
        plan_id = request.GET.get('plan_id')
        plan = Plan.objects.get(plan_id=plan_id)
        prj_list = Project.objects.all()
        env_list = Environment.objects.all()
        return render(request, 'platformpage/plan/update.html', {
            'plan': plan,
            'prj_list': prj_list,
            'env_list': env_list
        })

