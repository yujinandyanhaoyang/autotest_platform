from django.shortcuts import render
from platformpage.models import Sign
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

def sign_index(request):
    sign_list = Sign.objects.all()
    return render(request, "system/sign_index.html", {"sign_list": sign_list})

def sign_add(request):
    if request.method == 'POST':
        sign_name = request.POST['sign_name']
        description = request.POST['description']
        sign = Sign(sign_name=sign_name, description=description)
        sign.save()
        return HttpResponseRedirect("/platformpage/sign/")
    return render(request, "system/sign_add.html")

def sign_update(request):
    if request.method == 'POST':
        sign_id = request.POST['sign_id']
        sign_name = request.POST['sign_name']
        description = request.POST['description']
        Sign.objects.filter(sign_id=sign_id).update(sign_name=sign_name, description=description)
        return HttpResponseRedirect("/platformpage/sign/")
    sign_id = request.GET['sign_id']
    sign = Sign.objects.get(sign_id=sign_id)
    return render(request, "system/sign_update.html", {"sign": sign})