from django.shortcuts import render
from base.models import Interface, Project
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def interface_index(request):
    if_list = Interface.objects.all()
    return render(request, "base/interface/index.html", {"if_list": if_list})

def interface_add(request):
    if request.method == 'POST':
        if_name = request.POST['if_name']
        prj_id = request.POST['prj_id']
        project = Project.objects.get(prj_id=prj_id)
        url = request.POST['url']
        method = request.POST['method']
        data_type = request.POST['data_type']
        is_sign = request.POST['is_sign']
        description = request.POST['description']
        request_header_data = request.POST['request_header_data']
        request_body_data = request.POST['request_body_data']
        response_header_data = request.POST['response_header_data']
        response_body_data = request.POST['response_body_data']
        interface = Interface(if_name=if_name, url=url, project=project, method=method, data_type=data_type,
                          is_sign=is_sign, description=description, request_header_param=request_header_data,
                          request_body_param=request_body_data, response_header_param=response_header_data,
                          response_body_param=response_body_data)
        interface.save()
        return HttpResponseRedirect("/base/interface/")
    prj_list = Project.objects.all()
    return render(request, "base/interface/add.html", {"prj_list": prj_list})