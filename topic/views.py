import calendar
import json
import os
import time

from django.core import serializers

from django.http import JsonResponse, FileResponse

from student.models import Student
from teacher.models import Teacher
from topic.models import Topic


# 分页获取毕业选题
def list(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST访问', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    title = request.GET.get("title")
    page = (page - 1) * limit
    if title is None or title == '':
        total = Topic.objects.count()
        data = Topic.objects.all()[page:page + limit]
    else:
        total = Topic.objects.filter(title__contains=title).count()
        data = Topic.objects.filter(name__contains=title)[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'total': total})


# 学生添加选题
def add(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET访问', 'data': None})

    topic = Topic()
    # 根据学生id 查询该学生
    stu = Student.objects.filter(id=int(request.POST.get('id')))[0]
    tea = Teacher.objects.filter(id=int(request.POST.get('teacherId')))[0]
    s = Topic.objects.filter(stuId=stu.stuId)
    if len(s) > 0:
        if s[0].status in [0, 3]:
            # 修改
            return updateByStu(request=request)
        else:
            return JsonResponse({'code': 500, 'msg': '已提交过选题了', 'data': None})
    topic.stuId = stu.stuId
    topic.studentName = stu.name
    topic.title = request.POST.get('title')
    topic.content = request.POST.get('content')
    topic.teacherId = tea.id
    topic.teacherName = tea.name
    topic.status = 1
    # topic.topicFile = file.file
    file = request.FILES.get("files", None)
    if file is None:
        return JsonResponse({'code': 500, 'msg': '上传文件为空', 'data': None})
    fileName = calendar.timegm(time.gmtime())

    s = str(fileName) + '.' + file.name.split(".")[1]
    destination = open(os.path.join("static\\files\\" + s), 'wb+')
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    topic.topicFile = "static\\files\\" + s
    topic.save()
    return JsonResponse({'code': 0, 'msg': '添加成功', 'data': None})


# 学生查看自己的选题情况
def getByStuId(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST访问', 'data': None})
    try:
        stu = Student.objects.filter(id=int(request.GET.get('id')))
        topic = Topic.objects.filter(stuId=stu[0].stuId)
        return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", topic))})
    except Exception:
        return JsonResponse({'code': 500, 'msg': '未找到学生', 'data': None})


# 根据教师id 查看该老师下的学生选题情况
def getTopicById(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST访问', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    teacherId = int(request.GET.get("id"))
    page = (page - 1) * limit
    total = Topic.objects.count()
    data = Topic.objects.filter(teacherId=teacherId)[page:page + limit]

    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'total': total})


# 修改选题内容
def updateByStu(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持get访问', 'data': None})
    id = int(request.POST.get('id'))
    stu = Student.objects.filter(id=id)[0]
    topic = Topic.objects.filter(stuId=stu.stuId)[0]
    if topic.status in [1, 2]:
        return JsonResponse({'code': 500, 'msg': '暂时无法修改选题内容', 'data': None})
    title = request.POST.get('title')
    content = request.POST.get('content')
    teacherId = int(request.POST.get('teacherId'))

    file = request.FILES.get("files", None)
    if file is None:
        return JsonResponse({'code': 500, 'msg': '上传文件为空', 'data': None})
    fileName = calendar.timegm(time.gmtime())

    s = str(fileName) + '.' + file.name.split(".")[1]
    destination = open(os.path.join("static\\files\\" + s), 'wb+')
    for chunk in file.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()
    topicFile = "static\\files\\" + s


    tea = Teacher.objects.filter(id=teacherId)[0]
    # 提交审核
    Topic.objects.filter(id=topic.id).update(title=title, content=content, teacherId=teacherId, status=1,
                                             studentName=stu.name, teacherName=tea.name,topicFile=topicFile)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})


# 审核通过
def auditPass(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持get访问', 'data': None})
    id = int(request.POST.get("id"))
    Topic.objects.filter(id=id).update(status=2)
    return JsonResponse({'code': 0, 'msg': '通过成功', 'data': None})


# 打回
def auditReturn(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持get访问', 'data': None})
    id = int(request.POST.get("id"))
    # notes = request.POST.get('notes')
    Topic.objects.filter(id=id).update(status=3)
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': None})


# 根据学生学号 和教师id 查看学生已提交的选题情况
def getTopicByStuId(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST访问', 'data': None})
    stuId = request.GET.get("stuId")
    id = request.GET.get("id")  # 教师id
    querySet = Topic.objects.filter(stuId=stuId, teacherId=id).exclude(status=0)
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", querySet))})

# 下载文件
def download(request):
    id = request.GET.get("id")
    top = Topic.objects.filter(id=id)
    if len(top) == 0 or top[0].topicFile == '' or top[0].topicFile is None:
        return JsonResponse({'code': 500, 'msg': '该学生未提交文件', 'data': None})
    file = open(top[0].topicFile, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'application/octet-stream'
    lastName = str(top[0].stuId) + "." + top[0].topicFile.split(".")[1]
    response['Content-Disposition'] = 'attachment;filename='+lastName
    return response
