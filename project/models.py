from django.db import models

# Create your models here.
class Project(models.Model):
    project_id = models.CharField(primary_key=True, max_length=255, default='', verbose_name='项目编号')
    project_nickname = models.CharField(max_length=255, default='', verbose_name='登记时缩写')
    project_name = models.CharField(max_length=255, default='', verbose_name='项目名称')
    project_source = models.CharField(max_length=255, default='', verbose_name='项目来源')
    project_leader = models.CharField(max_length=255, default='', verbose_name='项目负责人')
    project_start_time = models.DateField(auto_now_add=True, verbose_name='项目开始日期')
    project_deadline = models.DateField(auto_now_add=True, verbose_name = '项目结束日期')
    project_kpi = models.IntegerField(default=0,verbose_name='指标数量')
    project_finish_kpi = models.IntegerField(default=0,verbose_name='完成指标数量')
    project_paper = models.IntegerField(default=0,verbose_name='挂靠论文序号')
    project_remarks = models.CharField(max_length=255, default='', verbose_name='备注')