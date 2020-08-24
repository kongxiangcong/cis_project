from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings    # 获取 settings.py 里边配置的信息
import os
from .models import *

# 1.1.前往 index 页（all）
def all_page(request):

    datas = Project.objects.all()
    content={'datas': datas}
    return render(request, 'project/all.html', content)

# # 3.2.查 - id
def search_project_id(request,project_id):
    project = Project.objects.filter(project_id = project_id)
    content = {'data': project}
    print(content)
    return render(request, 'project/project_detail.html', content)

def search_project_id_update(request,project_id):
    project = Project.objects.filter(project_id = project_id)
    content = {'data': project}
    print(content)
    return render(request, 'project/project_update.html', content)

@csrf_exempt
def update_confirm(request):
    if request.method == "GET":
        pproject_id = request.POST.get('project_id')
        update_obj = Project.objects.get(project_id=pproject_id)
        datas = Project.objects.all()
        content = {'datas': datas}
        print("render")
        return render(request, 'project/all.html', content)

    else:
        # 这里是post请求修改数据
        # 取新的名字
        new_name = request.POST.get('project_name')
        pproject_id = request.POST.get('project_id')
        new_name_nickname = request.POST.get('project_nickname')
        new_leader = request.POST.get('project_leader')
        new_source = request.POST.get('project_source')
        new_start_time = request.POST.get('project_start_time')
        new_kpi = request.POST.get('project_kpi')
        new_finish_kpi = request.POST.get('project_finish_kpi')
        new_paper = request.POST.get('project_paper')
        new_remarks = request.POST.get('project_remarks')

        print(new_remarks)
        # 更新信息,要用id来修改，所以提交的时候要传id过来
        update_obj = Project.objects.get(project_id=pproject_id)
        update_obj.project_name = new_name
        update_obj.project_nickname = new_name_nickname
        update_obj.project_leader = new_leader
        update_obj.project_source = new_source
        update_obj.project_start_time = new_start_time
        update_obj.project_kpi = new_kpi
        update_obj.project_finish_kpi = new_finish_kpi
        update_obj.project_paper = new_paper
        update_obj.project_remarks = new_remarks

        update_obj.save()   # 一定要执行，提交数据库保存~~~~~~

            #return redirect('project/all.html/')

        datas = Project.objects.all()
        content = {'datas': datas}
        print("redirect")
        return redirect('/project/allPage')

# # 1.2.前往 add 页
# def add_page( request ):
#     return render(request, 'student/add.html')
#
# # 2.增
# @csrf_exempt
# def add_student(request):
#     t_name = request.POST['tName']
#     t_age = request.POST['tAge']
#     t_image = request.FILES['tImage']
#     fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
#     with open(fname, 'wb') as pic:
#         for c in t_image.chunks():
#             pic.write(c)
#
#     student=student_info()
#     student.t_name=t_name
#     student.t_age=t_age
#     # 存访问路径到数据库
#     student.t_image = os.path.join("/static/media/", t_image.name)
#     student.save()
#
#     return redirect('/allPage')
#
# # 3.1.查 - name
# def search_student(request):
#     t_name = request.GET['q']
#     student=student_info.objects.filter(t_name=t_name)
#     content={'data':student}
#     return render(request,'student/all.html', content)
#


# # 4.改
# @csrf_exempt
# def update_student(request):
#
#     id=request.POST['t_id']
#     t_name = request.POST['tName']
#     t_age = request.POST['tAge']
#     # 缺陷：文件必传
#     t_image = request.FILES['tImage']
#
#     fname = os.path.join(settings.MEDIA_ROOT, t_image.name)
#     with open(fname, 'wb') as pic:
#         for c in t_image.chunks():
#             pic.write(c)
#     t_image = os.path.join("/static/media/", t_image.name)
#
#     student_info.objects.filter(id=id).update(t_name=t_name,t_age=t_age,t_image=t_image)
#     return redirect('/allPage')
#
# # 5.删
# def delete_student(request,student_id):
#     student_info.objects.filter(id=student_id).delete()
#     return redirect('/allPage')
