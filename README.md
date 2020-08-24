# cis_project

An effective way to manage the thesises and projects in CIS lab is through management system based on the Django framework.

## 环境
- 后端：Django + Python
- 前端：layui做界面设计
- 数据库：MySQL （Django+ORM模型实现数据库的映射），Navicat（可视化数据库操作）
- IDE：pycharm

**layui介绍**：
首先要熟悉HTML语法，主要作用是往页面上添加控件，每个控件有自己的属性。但是纯粹的HTML导入的控件，界面丑，不灵活，因此需要css+Js来给控件润色（boostrap）

可是有没有可视化的，或者已经写好漂亮的控件，提供给我们白痴直接调用呢。调研了一下市面上有layui，simpleui,easyui等等。这里以layui为例，根据文档可以快速实现输入框、按钮，导航栏、图标等控件样式

## 参考资料
- layui文档：https://www.layui.com/doc/element/color.html
- django+layui:https://blog.csdn.net/larger5/article/details/80905372
  
  本项目借鉴了上面博主的增删改查代码实现
- git教程：https://www.bilibili.com/video/BV1154y1B7c5?p=21&t=292
    
    为方便大家使用，采用git分布式实现项目合作开发
1. git下载
2. git配置

  用户信息
配置个人的用户名称和电子邮件地址：
```shell script
$ git config --global user.name "runoob"
$ git config --global user.email test@runoob.com
```
   Git 创建仓库
```shell script
$ git init
$ git status (查看当前目录下文件状态)
$ git add 文件 （把指定文件保存到暂存区）
$ git commit -m '提交注释' （把指定文件保存到工作区）
```
   Git 推到远程仓库
```shell script
$ git remote add origin 远程地址
$ git push origin master(推到远程仓库github上)
```

## 当前进度
实现了project的增删改操作

需要补充注册登录功能
1. 论文的增删改功能
2. 页面的美化（包括导航栏，侧边栏等等）
3. 最后实现查询功能（下拉框确定查询的类型）
4. 实现新增论文审核功能。

    审核的流程是：学生点击新增论文，填写基本的内容和上次PDF后，点击提交审核。
系统接收到提交后发邮件给管理员通知管理员上系统查看。管理员审核论文，补充项目号，审核通过/失败。系统获取后邮件通知学生进行修改/查看。