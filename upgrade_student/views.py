import datetime
import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from upgrade_student.models import UpgradeStudent

# 分页查询
def getUpgradeStudent(request):
    if request.method!='GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    name = request.GET.get("name")
    page = (page - 1) * limit
    if name =='' or name is None:
        total = UpgradeStudent.objects.filter().count()
        data = UpgradeStudent.objects.filter()[page:page + limit]
    else:
        total = UpgradeStudent.objects.filter(name__contains=name).count()
        data = UpgradeStudent.objects.filter(name__contains=name)[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'count': total})


#  根据id 查询
def getById(request):
    if request.method!='GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    id = int(request.GET.get("id"))
    poor = UpgradeStudent.objects.filter(id=id)
    if len(poor)==0:
        return JsonResponse({'code': 500, 'msg': '未找到', 'data': None})
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", poor))})

# 删除
def deleted(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    ids = eval(request.POST.get("ids"))
    if len(ids) == 0:
        return JsonResponse({'code': 500, 'msg': '请选择需要删除的记录', 'data': None})
    UpgradeStudent.objects.filter(id__in=ids).delete()
    return JsonResponse({'code': 0, 'msg': '删除成功', 'data': None})

#  添加
def save(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    name = request.POST.get("name")
    stuId = request.POST.get("stuId")
    upgrade_time = request.POST.get("upgrade_time")
    stu = UpgradeStudent()
    stu.name = name
    stu.stuId = stuId
    stu.upgrade_time = upgrade_time
    tempTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    stu.create_time = tempTime
    stu.update_time = tempTime
    stu.save()
    return JsonResponse({'code': 0, 'msg': '添加成功', 'data': None})


#  修改
def update(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    id = request.POST.get("id")
    upgrade_time = request.POST.get("upgrade_time")
    tempTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    UpgradeStudent.objects.filter(id=id).update(upgrade_time=upgrade_time, update_time=tempTime)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})