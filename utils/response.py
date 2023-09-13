import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse


# 统一响应对象
class Response:
    code = 0
    data = None
    msg = ''

    def __init__(self, code, data, msg):
        self.code = code
        self.data = data
        self.msg = msg

    def __init__(self):
        pass

    # 返回json
    def json(self):
        return JsonResponse(self.__dict__, safe=False)
        # return JsonResponse(json.dumps(self.__dict__,ensure_ascii=False), content_type="application/json")

    # 失败
    def fail(self, msg='接口错误请联系管理员'):
        self.code = 500
        self.msg = msg
        return self.json()

    # 请求成功
    def success(self, data=None, msg='请求成功'):
        self.code = 0
        self.data = data
        self.msg = msg
        return self.json()

