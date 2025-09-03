from django.shortcuts import render
from platformpage.models import Report, Plan

def report_index(request):
    plan_id = request.GET['plan_id']
    report = Report.objects.get(plan_id=plan_id)
    report_content = eval(report.content)
    return render(request, "report.html", {"report": report, "report_content": report_content})