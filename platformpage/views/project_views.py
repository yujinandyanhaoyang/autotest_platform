from django.shortcuts import render
from platformpage.models import Project, Sign
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib import messages


def project_index(request):
    prj_list = Project.objects.all()
    return render(request, "platformpage/project/index.html", {"prj_list": prj_list})

def project_add(request):
    if request.method == 'POST':
        prj_name = request.POST['prj_name']
        name_same = Project.objects.filter(prj_name=prj_name)
        if name_same:
            messages.error(request, "项目已存在")
        else:
            description = request.POST['description']
            sign_id = request.POST['sign']
            sign = Sign.objects.get(sign_id=sign_id)
            prj = Project(prj_name=prj_name, description=description, sign=sign)
            prj.save()
            return HttpResponseRedirect("/platformpage/project/")
    sign_list = Sign.objects.all()
    return render(request, "platformpage/project/add.html", {"sign_list": sign_list})

def project_update(request):
    if request.method == 'POST':
        prj_id = request.POST['prj_id']
        prj_name = request.POST['prj_name']
        name_exit = Project.objects.filter(prj_name=prj_name).exclude(prj_id=prj_id)
        if name_exit:
            return HttpResponse("项目已存在")
        else:
            description = request.POST['description']
            sign_id = request.POST['sign_id']
            sign = Sign.objects.get(sign_id=sign_id)
            Project.objects.filter(prj_id=prj_id).update(prj_name=prj_name, description=description,sign=sign)
            return HttpResponseRedirect("/platformpage/project/")
    prj_id = request.GET['prj_id']
    prj = Project.objects.get(prj_id=prj_id)
    sign_list = Sign.objects.all()
    return render(request, "platformpage/project/update.html", {"prj": prj, "sign_list": sign_list})

def project_delete(request):
    if request.method == 'GET':
        prj_id = request.GET['prj_id']
        Project.objects.filter(prj_id=prj_id).delete()
        return HttpResponseRedirect("/platformpage/project/")

