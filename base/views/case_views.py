from django.shortcuts import render
from base.models import Case, Project
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from lib.execute import Execute

def case_index(request):
    case_list = Case.objects.all()
    return render(request, "base/case/index.html", {"case_list": case_list})

def case_add(request):
    if request.method == 'POST':
        case_name = request.POST['case_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        description = request.POST['description']
        content = request.POST['content']
        case = Case(case_name=case_name, project=project, description=description, content=content)
        case.save()
        return HttpResponseRedirect("/base/case/")
    prj_list = Project.objects.all()
    return render(request, "base/case/add.html", {"prj_list": prj_list})

def case_run(request):
    if request.method == 'POST':
        case_id = request.POST['case_id']
        env_id = request.POST['env_id']
        execute = Execute(case_id, env_id)
        case_result = execute.run_case()
        return JsonResponse(case_result)