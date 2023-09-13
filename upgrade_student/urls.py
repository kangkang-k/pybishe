
from django.urls import re_path
from . import views

# 路由 /upgradeStudent
urlpatterns = [
    re_path('getUpgradeStudent', views.getUpgradeStudent), # 分页查询
    re_path('getById', views.getById), #  根据id 查询
    re_path('deleted', views.deleted), # 删除
    re_path('save', views.save), # 添加
    re_path('update', views.update), # 修改
]
