import logging

from django.dispatch.dispatcher import logger
from django.http import JsonResponse
from django.middleware.common import MiddlewareMixin


# 全局异常处理
class CustomException(MiddlewareMixin):
    def process_exception(self, request, exception):
        """
        统一异常处理
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        logger.exception(exception)
        return JsonResponse({'code': 500, 'msg': '接口异常请联系管理员', 'data': None})
