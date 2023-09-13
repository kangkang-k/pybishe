
from django.urls import path
from . import views

# 路由 /attendance
urlpatterns = [
    path('getAttendance', views.getAttendance), #  分页查询
    path('getById', views.getById), #  根据id 查询
    path('deleted', views.deleted), # 删除
    path('save', views.save), # 添加
    path('update', views.update), # 修改
]
