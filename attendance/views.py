import datetime
import json

from django.core import serializers
from django.http import JsonResponse

from attendance.models import Attendance


# 分页查询
def getAttendance(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    page = (page - 1) * limit
    total = Attendance.objects.filter().count()
    data = Attendance.objects.filter()[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'count': total})


#  根据id 查询
def getById(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持post请求', 'data': None})
    id = int(request.GET.get("id"))
    admin = Attendance.objects.filter(id=id)
    if len(admin) == 0:
        return JsonResponse({'code': 500, 'msg': '未找到', 'data': None})
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", admin))})


# 删除
def deleted(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    ids = eval(request.POST.get("ids"))
    if len(ids) == 0:
        return JsonResponse({'code': 500, 'msg': '请选择需要删除的记录', 'data': None})
    Attendance.objects.filter(id__in=ids).delete()
    return JsonResponse({'code': 0, 'msg': '删除成功', 'data': None})


#  添加
def save(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    course_name = request.POST.get("course_name")
    late = request.POST.get("late")
    late_time = request.POST.get("late_time")
    create_time = request.POST.get("create_time")
    signIn = request.POST.get("signIn")
    addtend = Attendance()
    addtend.course_name = course_name
    addtend.late = late
    addtend.late_time = late_time
    addtend.create_time = create_time
    addtend.signIn = signIn
    tempTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    addtend.create_time = tempTime
    addtend.save()
    return JsonResponse({'code': 0, 'msg': '添加成功', 'data': None})


#  修改
def update(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET请求', 'data': None})
    id = request.POST.get("id")
    course_name = request.POST.get("course_name")
    late = request.POST.get("late")
    late_time = int(request.POST.get("late_time"))
    Attendance.objects.filter(id=id).update(course_name=course_name, late=late, late_time=late_time)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})
