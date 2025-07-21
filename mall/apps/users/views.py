import json
import re

from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

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
        if not re.match('[a-zA-Z]{5,20}', username):
            return JsonResponse({'code':400, 'errmsg':'用户名不符合规则'})
        if not re.match('^(?=.*[A-Za-z])(?=.*\d).{8,}$', password):
            return JsonResponse({'code':400, 'errmsg':'密码不符合规则'})
        if not password == password2:
            return JsonResponse({'code':400, 'errmsg':'两次密码需一样'})
        if not re.match('^1[3-9]\d{9}$', mobile):
            return JsonResponse({'code':400, 'errmsg':'请输入正确的电话号码'})

        user = User.objects.get(username=username)
        if user:
            return JsonResponse({'code':400, 'errmsg':'用户名重复'})

        try:
            User.objects.create_user(username=username, password=password, mobile=mobile, sms_code=sms_code)
        except Exception as e:
            return JsonResponse({'code':400, 'errmsg':e})

        return JsonResponse({'code':0, 'errmsg':'ok'})
