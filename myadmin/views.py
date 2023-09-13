import datetime
import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from myadmin.models import MyAdmin

# 分页查询
from utils import utils


def getAdmin(request):
    if request.method!='GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    page = (page - 1) * limit
    name = request.GET.get("name")
    if name =='' or name is None:
        total = MyAdmin.objects.filter().count()
        data = MyAdmin.objects.filter()[page:page + limit]
    else:
        total = MyAdmin.objects.filter(name__contains=name).count()
        data = MyAdmin.objects.filter(name__contains=name)[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'count': total})


#  根据id 查询
def getById(request):
    if request.method!='GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    id = int(request.GET.get("id"))
    admin = MyAdmin.objects.filter(id=id)
    if len(admin)==0:
        return JsonResponse({'code': 500, 'msg': '未找到', 'data': None})
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", admin))})

# 删除
def deleted(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    ids = eval(request.POST.get("ids"))
    if len(ids) == 0:
        return JsonResponse({'code': 500, 'msg': '请选择需要删除的记录', 'data': None})
    MyAdmin.objects.filter(id__in=ids).delete()
    return JsonResponse({'code': 0, 'msg': '删除成功', 'data': None})

#  添加
def save(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    name = request.POST.get("name")
    password = utils.getPassword(request.POST.get("password"))
    remarks = request.POST.get("remarks")
    email = request.POST.get("email")
    admin = MyAdmin()
    admin.name = name
    admin.password = password
    admin.email = email
    admin.remarks = remarks
    tempTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    admin.create_time = tempTime
    admin.update_time = tempTime
    admin.save()
    return JsonResponse({'code': 0, 'msg': '添加成功', 'data': None})


#  修改
def update(request):
    if request.method!='POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    id = request.POST.get("id")
    name = request.POST.get("name")
    password = request.POST.get("password")
    email = request.POST.get("email")
    remarks = request.POST.get("remarks")
    tempTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if password =='' or password is None:
        MyAdmin.objects.filter(id=id).update(name=name,email=email,update_time=tempTime,remarks=remarks)
    else:
        password = utils.getPassword(password)
        MyAdmin.objects.filter(id=id).update(name=name, email=email, update_time=tempTime,password=password,remarks=remarks)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})