import json

from django.core import serializers
from django.http import JsonResponse

import utils.utils
from teacher.models import Teacher

from topic.models import Topic


# 获取所有老师信息
def getAllTeacher(request):
    list = Teacher.objects.all()
    res = json.loads(serializers.serialize("json", list))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': res})


# 教师列表查询
def list(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST访问', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    page = (page - 1) * limit
    name = request.GET.get("name")
    if name is None or name == '':
        total = Teacher.objects.count()
        data = Teacher.objects.all()[page:page + limit]
    else:
        total = Teacher.objects.filter(name__contains=name).count()
        data = Teacher.objects.filter(name__contains=name)[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'total': total})

# 添加老师
def addTeacher(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET访问', 'data': None})
    teacher = Teacher()
    teacher.name = request.POST.get('name')
    tea = Teacher.objects.filter(name=teacher.name)
    if len(tea)>0:
        return JsonResponse({'code': 500, 'msg': teacher.name+'教师账号已存在', 'data': None})
    password = request.POST.get('password')
    if password is None or password == '':
        password = 'e10adc3949ba59abbe56e057f20f883e'
    teacher.password = utils.utils.getPassword(str(password))
    teacher.save()
    return JsonResponse({'code': 0, 'msg': '添加成功', 'data': None})

# 修改老师信息
def update(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET访问', 'data': None})
    name = request.POST.get('name')
    id = request.POST.get('id')
    tea = Teacher.objects.filter(name=name).exclude(id=id)
    if len(tea)>0:
        return JsonResponse({'code': 500, 'msg': name+'教师账号已存在', 'data': None})
    password = request.POST.get('password')
    if password == '' or password is None:
        Teacher.objects.filter(id=id).update(name=name)
    else:
        Teacher.objects.filter(id=id).update(name=name, password=password)
    Topic.objects.filter(teacherId=id).update(teacherName=name)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})