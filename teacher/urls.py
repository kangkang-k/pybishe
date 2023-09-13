
from django.urls import re_path
from . import views

# 路由
urlpatterns = [
    re_path('list', views.getAllTeacher), # 获取所有老师信息
    re_path('addTeacher', views.addTeacher), #  添加老师
    re_path('listPage', views.list), # 教师列表查询
    re_path('update', views.update), # 修改教师信息
]
