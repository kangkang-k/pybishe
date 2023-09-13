from django.http import HttpResponse, JsonResponse

from myadmin.models import MyAdmin
from student.models import Student
from teacher.models import Teacher
from utils import utils
from utils.response import Response


# 用户通用登录
def login(request):
    if request.method == 'POST':
        #将原密码进行md5加密并获取加密后的密码
        password = utils.getPassword(request.POST.get('password'))
        role = int(request.POST.get('role'))
        if role == 0:
            name = request.POST.get('name')
            user = stuLogin(name, password)
        elif role == 1:
            name = request.POST.get('name')
            user = teaLogin(name, password)
        else:
            name = request.POST.get('name')
            user = adminLogin(name, password)
        if len(user) > 0:
            return JsonResponse({'code': 0, 'msg': '登录成功', 'data': user[0].id})
        else:
            return JsonResponse({'code': 500, 'msg': '账号或密码错误', 'data': None})
    else:
        return JsonResponse({'code': 500, 'msg': '不支持GET提交', 'data': None})


# 学生登录
def stuLogin(name, password):
    stu = Student.objects.filter(stuId=name, password=password)
    return stu


# 教师登录
def teaLogin(name, password):
    tea = Teacher.objects.filter(name=name, password=password)
    return tea


# 管理登录
def adminLogin(name, password):
    admin = MyAdmin.objects.filter(name=name, password=password)
    return admin
