from django.urls import re_path
from django.urls import re_path, include
from . import views

# 路由
urlpatterns = [
    re_path('login', views.login),  # 用户通用登录
    re_path(r'^student/', include('student.urls')),
    re_path(r'^topic/', include('topic.urls')),
    re_path(r'^teacher/', include('teacher.urls')),
    re_path(r'^upgradeStudent/', include('upgrade_student.urls')),
    re_path(r'^admin/', include('myadmin.urls')),
    re_path(r'^attendance/', include('attendance.urls')),
]
