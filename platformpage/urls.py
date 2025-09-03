"""
URL configuration for Autotest_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.platformpage, name='platformpage')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='platformpage')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from platformpage.views import findata
from platformpage.views.sign_views import sign_index, sign_add, sign_update
from platformpage.views.project_views import project_index, project_add, project_update, project_delete
from platformpage.views.case_views import case_update, case_uplode, case_delete, case_index, case_add, case_run
from platformpage.views.download_report_views import download_report
from platformpage.views.env_views import env_delete, env_index, env_add, env_update
from platformpage.views.interface_views import interface_delete, interface_update, interface_index, interface_add
from platformpage.views.plan_views import plan_update, plan_delete, plan_index, plan_add, plan_run

urlpatterns = [
    # 项目管理
    path("project/", project_index),
    path("project_add/", project_add),
    path("project_update/", project_update),
    path("project_delete/", project_delete),

    # 签名管理
    path("sign/", sign_index),
    path("sign_add/", sign_add),
    path("sign_update/", sign_update),

    # 环境管理
    path("env/", env_index),
    path("env_add/", env_add),
    path("env_update/", env_update),
    path("env_delete/", env_delete),

    # 接口管理
    path("interface/", interface_index),
    path("interface_add/", interface_add),
    path("interface_update/", interface_update),
    path("interface_delete/", interface_delete),

    # 用例管理
    path("case/", case_index),
    path("case_add/", case_add),
    path("case_run/", case_run),
    path("case_update/", case_update),
    path("case_delete/", case_delete),
    path("case_uplode/", case_uplode),

    # 计划管理
    path("plan/", plan_index),
    path("plan_add/", plan_add),
    path("plan_run/", plan_run),
    path("plan_update/", plan_update),
    path("plan_delete/", plan_delete),

    # 测试报告
    # path("report/", report_index),
    # 现在假设点击这个路径后会直接下载我们的报告文件
    path("report/", download_report),

    # 数据管理
    path("findata/", findata)
]

