import json
import re

from django.contrib.auth import login
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha

from apps.users.models import User


# Create your views here.
class RegisterView(View):
    def post(self, request):
        body_str=request.body.decode()
        body_dict=json.loads(body_str)

        username = body_dict['username']
        password = body_dict['password']
        password2 = body_dict['password2']
        mobile = body_dict['mobile']
        sms_code = body_dict['sms_code']
        allow = body_dict['allow']

        if not all([username,password,password2,mobile,sms_code,allow]):
            return JsonResponse({'code':400, 'errmsg':'参数不全'})
        if not re.match('^[a-zA-Z0-9_-]{5,20}$', username) or re.match('^[0-9]+$', username):
            return JsonResponse({'code':400, 'errmsg':'用户名必须是5-20个字符（字母、数字、_、-）且不能为纯数字'})
        if not re.match('^(?=.*[A-Za-z])(?=.*\d).{8,}$', password):
            return JsonResponse({'code':400, 'errmsg':'密码不符合规则'})
        if not password == password2:
            return JsonResponse({'code':400, 'errmsg':'两次密码需一样'})
        if not re.match('^1[3-9]\d{9}$', mobile):
            return JsonResponse({'code':400, 'errmsg':'请输入正确的电话号码'})

        user = User.objects.filter(username=username)
        if user:
            return JsonResponse({'code':400, 'errmsg':'用户名重复'})

        try:
            User.objects.create_user(username=username, password=password, mobile=mobile)
        except Exception as e:
            return JsonResponse({'code':400, 'errmsg':f'{e}'})

        login(request, user)

        return JsonResponse({'code':0, 'errmsg':'ok'})



