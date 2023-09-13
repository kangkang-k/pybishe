from django.urls import re_path
from . import views

# 路由
urlpatterns = [
    re_path('register', views.register), # 学生注册
    re_path('getById', views.getById), # 根据id 查询学生信息
    re_path('getByStudentId', views.getByStudentId), # 根据id 查询学生信息
    re_path('list', views.listStu), # 学生列表查询
    re_path('delete', views.deleteStudent), # 删除学生 格式 [1,2]
    re_path('getTeaching', views.getTeaching), # 毕业生教学任务查询
    re_path('updateById', views.updateById), # 修改学生信息
    re_path('getAllStudent', views.getAllStudent) # 获取所有学生信息
]
