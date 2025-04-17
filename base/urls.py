"""EasyTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path

from base.views import project_index, project_add, project_update, project_delete, sign_index, sign_add, sign_update, \
    env_index, env_add, env_update, interface_add, interface_index, case_index, case_add, case_run, plan_index, \
    plan_add, plan_run, report_index, findata

urlpatterns = [
    # 项目管理
    path('project/', project_index),
    path('project_add/', project_add),
    path('project_update/', project_update),
    path('project_delete/', project_delete),

    # 签名管理
    path('sign/', sign_index),
    path('sign_add/', sign_add),
    path('sign_update/', sign_update),

    # 环境管理
    path('env/', env_index),
    path('env_add/', env_add),
    path('env_update/', env_update),

    # 接口管理
    path('interface/', interface_index),
    path('interface_add/', interface_add),

    # 用例管理
    path('case/', case_index),
    path('case_add/', case_add),
    path('case_run/', case_run),

    # 计划管理
    path('plan/', plan_index),
    path('plan_add/', plan_add),
    path('plan_run/', plan_run),

    # 测试报告
    path('report/', report_index),
    # 数据管理
    path('findata/', findata)
]

