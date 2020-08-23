"""cis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from project import views as project_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^project/allPage/$', project_views.all_page),  # 前往所有学生的网页
    url(r'^project/detail/(?P<project_id>\w+)/$', project_views.search_project_id),  # 根据 id 查找学生的 dao 操作
    url(r'^project/update/(?P<project_id>\w+)/$', project_views.search_project_id_update),
    # url(r'^get/(?P<project_id>[0-9]*)/$', views.search_project_id)
]
