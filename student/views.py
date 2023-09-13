from django.db import transaction
from django.http import JsonResponse
import json
from django.core import serializers
from student.models import Student

from topic.models import Topic
from utils import utils


# 学生注册
def register(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET注册', 'data': None})
    stu = Student()
    stu.stuId = request.POST.get('stuId')
    stu.name = request.POST.get('name')
    password = request.POST.get('password')
    student = getByStuId(stu.stuId)
    if student is not None:
        return JsonResponse({'code': 500, 'msg': "学生id为:" + stu.stuId + "已经存在", 'data': None})
    if password is None or password == '':
        # 默认密码
        password = 'e10adc3949ba59abbe56e057f20f883e'

    stu.password = utils.getPassword(str(password))
    stu.save()
    return JsonResponse({'code': 0, 'msg': '注册成功', 'data': None})


# 学生列表查询
def listStu(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST请求', 'data': None})
    page = int(request.GET.get("page"))
    limit = int(request.GET.get("limit"))
    name = request.GET.get("name")
    page = (page - 1) * limit
    if name is None or name == '':
        total = Student.objects.count()
        data = Student.objects.all()[page:page + limit]
    else:
        total = Student.objects.filter(name__contains=name).count()
        data = Student.objects.filter(name__contains=name)[page:page + limit]
    data = json.loads(serializers.serialize("json", data))
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': data, 'count': total})


# 根据id 查询用户信息
def getById(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST请求', 'data': None})
    id = request.GET.get("id")
    stuList = Student.objects.filter(id=id)
    if len(stuList) > 0:
        return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", stuList))})
    return JsonResponse({'code': 500, 'msg': '没有该id学生', 'data': None})


# 根据id 查询用户信息
def getByStudentId(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持POST请求', 'data': None})
    stuId = request.GET.get("stuId")
    stuList = Student.objects.filter(stuId=stuId)
    if len(stuList) > 0:
        return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", stuList))})
    return JsonResponse({'code': 500, 'msg': '没有该id学生', 'data': None})


# 删除学生 添加了事务
@transaction.atomic
def deleteStudent(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持GET提交', 'data': None})
    ids = eval(request.POST.get("ids"))
    if len(ids) == 0:
        return JsonResponse({'code': 500, 'msg': '请选择需要删除的学生', 'data': None})
    stuList = Student.objects.all()

    for stu in stuList:
        if stu.id in ids:
            Student.objects.filter(stuId=stu.stuId).delete()
            Topic.objects.filter(stuId=stu.stuId).delete()
    return JsonResponse({'code': 0, 'msg': '删除成功', 'data': None})


# 毕业生教学任务查询
def getTeaching(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '不支持post提交', 'data': None})
    stu = getStudentById(int(request.GET.get("id")))
    if stu is None:
        return JsonResponse({'code': 500, 'msg': '没有该学生', 'data': None})
    data = {
        '已修学分': stu.s1,
        '未修学分': stu.s2,
        '必修学分': stu.s3,
    }
    return JsonResponse({'code': 0, 'msg': '', 'data': data})


# 根据id 修改学生信息
def updateById(request):
    if request.method != 'POST':
        return JsonResponse({'code': 500, 'msg': '不支持get提交', 'data': None})
    name = request.POST.get("name")
    stuId = request.POST.get("stuId")
    s1 = request.POST.get("s1")
    s2 = request.POST.get("s2")
    s3 = request.POST.get("s3")
    password = utils.getPassword(str(request.POST.get("password")))
    college = request.POST.get("college")
    speciality = request.POST.get("speciality")
    if password == '' or password is None:
        Student.objects.filter(stuId=stuId).update(name=name, s1=s1, s2=s2, s3=s3, college=college,
                                                   speciality=speciality)
    else:
        Student.objects.filter(stuId=stuId).update(name=name, password=password, s1=s1, s2=s2, s3=s3, college=college,
                                                   speciality=speciality)
    Topic.objects.filter(stuId=stuId).update(studentName=name)
    return JsonResponse({'code': 0, 'msg': '修改成功', 'data': None})

# 获取所有学生信息
def getAllStudent(request):
    if request.method != 'GET':
        return JsonResponse({'code': 500, 'msg': '只支持get访问', 'data': None})
    list = Student.objects.filter().all()
    return JsonResponse({'code': 0, 'msg': '请求成功', 'data': json.loads(serializers.serialize("json", list))})

# 根据 学生id 查询学生基本信息
def getByStuId(stuId):
    stuList = Student.objects.filter(stuId=stuId)
    if len(stuList) > 0:
        return stuList[0]
    return None


# 根据 id 查询学生基本信息
def getStudentById(id):
    stuList = Student.objects.filter(id=id)
    if len(stuList) > 0:
        return stuList[0]
    return None


