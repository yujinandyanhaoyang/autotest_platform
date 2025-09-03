from django.shortcuts import render
from django.http import HttpResponseRedirect
from platformpage.models import Environment, Project


def env_index(request):
    env_list = Environment.objects.all()
    return render(request, "platformpage/env/index.html", {"env_list": env_list})

def env_add(request):
    if request.method == 'POST':
        env_name = request.POST['env_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        url = request.POST['url']
        private_key = request.POST['private_key']
        description = request.POST['description']
        env = Environment(env_name=env_name, url=url, project=project,
                           private_key=private_key, description=description)
        env.save()
        return HttpResponseRedirect("/platformpage/env/")
    prj_list = Project.objects.all()
    return render(request, "platformpage/env/add.html", {"prj_list": prj_list})

def env_update(request):
    # print('环境更改函数已接收请求')
    if request.method == 'POST':
        # print('正在修改')
        env_id = request.POST['env_id']
        env_name = request.POST['env_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        url = request.POST['url']
        private_key = request.POST['private_key']
        description = request.POST['description']
        Environment.objects.filter(env_id=env_id).update(env_name=env_name, url=url, project=project, private_key=private_key, description=description)
        return HttpResponseRedirect("/platformpage/env/")
    env_id = request.GET['env_id']
    env = Environment.objects.get(env_id=env_id)
    prj_list = Project.objects.all()
    return render(request, "platformpage/env/update.html", {"env": env, "prj_list": prj_list})


def env_delete(request):
    if request.method == 'GET':
        env_id = request.GET['env_id']
        Environment.objects.filter(env_id=env_id).delete()
        return HttpResponseRedirect("/platformpage/env/")