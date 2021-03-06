# Generated by Django 3.0.3 on 2020-08-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.CharField(default='', max_length=255, primary_key=True, serialize=False, verbose_name='项目编号')),
                ('project_nickname', models.CharField(default='', max_length=255, verbose_name='登记时缩写')),
                ('project_name', models.CharField(default='', max_length=255, verbose_name='项目名称')),
                ('project_source', models.CharField(default='', max_length=255, verbose_name='项目来源')),
                ('project_leader', models.CharField(default='', max_length=255, verbose_name='项目负责人')),
                ('project_start_time', models.DateField(auto_now_add=True, verbose_name='项目开始日期')),
                ('project_deadline', models.DateField(auto_now_add=True, verbose_name='项目结束日期')),
                ('project_kpi', models.IntegerField(default=0, verbose_name='指标数量')),
                ('project_finish_kpi', models.IntegerField(default=0, verbose_name='完成指标数量')),
                ('project_paper', models.IntegerField(default=0, verbose_name='挂靠论文序号')),
                ('project_remarks', models.CharField(default='', max_length=255, verbose_name='备注')),
            ],
        ),
    ]
