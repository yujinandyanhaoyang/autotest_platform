import json

from django.shortcuts import render
from platformpage.models import Interface, Project
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def interface_index(request):
    if_list = Interface.objects.all()
    return render(request, "platformpage/interface/index.html", {"if_list": if_list})

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
        return HttpResponseRedirect("/platformpage/interface/")
    prj_list = Project.objects.all()
    return render(request, "platformpage/interface/add.html", {"prj_list": prj_list})

def interface_update(request):
    print('已经接收到请求，开始更新')
    if request.method == 'POST':
        print(f'请求方法是{request.method},\n')
        print(f'具体prj_id的参数信息是{request.POST["prj_id"]}')
        print(f'具体url的参数信息是{request.POST["url"]}')
        print(f'具体data_type的参数信息是{request.POST["data_type"]}')
        # print(f'具体if_name的参数信息是{request.POST["if_name"]}')
        print(f'具体if_id的参数信息是{request.POST["if_id"]}')

        if_id = request.POST['if_id']
        # if_name = request.POST['if_name']#暂不处理
        prj_id = request.POST['prj_id']
        url = request.POST['url']
        method = request.POST['method']
        data_type = request.POST['data_type']
        is_sign = request.POST['is_sign']
        description = request.POST['description']
        request_header_data = request.POST['request_header_data']
        request_body_data = request.POST['request_body_data']
        response_header_data = request.POST['response_header_data']
        response_body_data = request.POST['response_body_data']
        Interface.objects.filter(if_id=if_id).update( url=url, method=method, data_type=data_type,
                                              is_sign=is_sign, description=description,prj_id=prj_id,
                                              request_header_param=request_header_data,
                                              request_body_param=request_body_data,
                                              response_header_param=response_header_data,
                                              response_body_param=response_body_data)
        return HttpResponseRedirect("/platformpage/interface/")
    print(f'请求方法是{request.method},具体的参数信息是{request.GET.get("if_id")}')
    print(f'先跳转表单页面更新数据，完成数据更新后使用POST方法提交新的表单')
    if_id = request.GET['if_id']
    if_info = Interface.objects.get(if_id=if_id)
    prj_list = Project.objects.all()
    # print(f'所属项目列表：{prj_list}，索引到的表格:{if_info}')
    # print(f'表格中的具体参数{if_info.request_header_param}')
    print(f'表格中if_info.response_body_param的具体参数{if_info.response_body_param}')
    print(f'表格中if_info.if_id的具体参数{if_info.if_id}')

    # 解析四个字段
    request_header = parse_json_field(if_info.request_header_param)
    request_body = parse_json_field(if_info.request_body_param)
    response_body = parse_json_field(if_info.response_body_param)
    response_head = parse_json_field(if_info.response_header_param)
    return render(request, "platformpage/interface/update.html", {
        "if_info": if_info,
        "prj_list": prj_list,
        "request_header": request_header,
        "request_body": request_body,
        "response_body": response_body,
        "response_head": response_head
    })
# 定义通用的解析函数将数据列表转成json格式
def parse_json_field(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return []

def interface_delete(request):
    if request.method == 'GET':
        if_id = request.GET['if_id']
        Interface.objects.get(if_id=if_id).delete()
        return HttpResponseRedirect("/platformpage/interface/")

