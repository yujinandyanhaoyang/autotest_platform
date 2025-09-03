from base.models import Interface, Environment, Case
from django.http import JsonResponse

def findata(request):
    if request.method == 'GET':
        get_type = request.GET["type"]
        if get_type == "get_all_if_by_prj_id":
            prj_id = request.GET["prj_id"]
            if_list = Interface.objects.filter(project=prj_id).all().values()
            return JsonResponse(list(if_list), safe=False)
        if get_type == "get_if_by_if_id":
            if_id = request.GET["if_id"]
            interface = Interface.objects.filter(if_id=if_id).values()
            return JsonResponse(list(interface), safe=False)
        if get_type == "get_env_by_prj_id":
            prj_id = request.GET["prj_id"]
            env_list = Environment.objects.filter(project_id=prj_id).values()
            return JsonResponse(list(env_list), safe=False)
        if get_type == "get_all_case_by_prj_id":
            prj_id = request.GET["prj_id"]
            case_list = Case.objects.filter(project_id=prj_id).values()
            return JsonResponse(list(case_list), safe=False)