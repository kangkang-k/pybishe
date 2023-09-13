from django.urls import re_path, include
from . import views

# 路由
urlpatterns = [
    re_path('list', views.list),  # 分页获取毕业选题
    re_path('add', views.add),  # 学生添加选题
    re_path('saveTopic', views.add),  # 学生提交选题
    re_path('getTopicById', views.getTopicById),  # 根据教师id 查看该老师下的学生选题情况
    re_path('updateByStu', views.updateByStu),  # 学生修改选题内容
    re_path('getTopicByStuId', views.getTopicByStuId),  # 根据学生学号 和教师id 查看学生已提交的选题情况
    re_path('getByStuId', views.getByStuId),  # 学生查看自己的选题情况
    re_path('auditPass', views.auditPass),  # 教师通过审核
    re_path('auditReturn', views.auditReturn),  # 教师打回
    re_path('download', views.download),  # 下载附件
]
