import json
import re

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection

from apps.users.utils import generic_email_verify_token, check_verify_token

from libs.captcha.captcha import captcha

from apps.users.models import User
from mall import settings
from utils.mixins import LoginRequiredJsonMixin


# Create your views here.
class RegisterView(View):
    def post(self, request):
        body_str=request.body.decode()
        body_dict=json.loads(body_str)

        username = body_dict.get('username')
        password = body_dict.get('password')
        password2 = body_dict.get('password2')
        mobile = body_dict.get('mobile')
        sms_code = body_dict.get('sms_code')
        allow = body_dict.get('allow')

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

        # session
        login(request, user)

        return JsonResponse({'code':0, 'errmsg':'ok'})

class LoginView(View):
    def post(self, request):
        data=json.loads(request.body.decode())
        username=data.get('username')
        password=data.get('password')
        remebered=data.get('remebered')

        if not all([username,password]):
            return JsonResponse({'code':400, 'errmsg':'参数不全'})

        # method1: db
        # method2: 本质上也是db
        # 手机号作为用户名登录User(AbstractUser)
        if re.match('1[3-9]\d{9}', username):
            User.USERNAME_FIELD='mobile'
        else:
            User.USERNAME_FIELD='username'
        user = authenticate(username=username,password=password)
        if user is None:
            return JsonResponse({'code':400, 'errmsg':'账号或密码错误'})

        # session
        login(request, user)

        # 记住登录
        if remebered is not None:
            # None默认两周过期
            request.session.set_expiry(None)
        else:
            # 浏览器关闭session过期
            request.session.set_expiry(0)

        response = JsonResponse({'code':0, 'errmsg':'ok'})
        response.set_cookie('username', username, max_age=2*7*24*3600)

        return response

class LogoutView(View):
    def delete(self, request):
        #DELETE
        logout(request)
        response=JsonResponse({'code':0, 'errmsg':'ok'})
        response.delete_cookie('username')

        return response

# 装饰器、多继承

class CenterView(LoginRequiredJsonMixin, View):
    def get(self, request):
        return JsonResponse({'code':0, 'errmsg':'ok'})

class EmailView(LoginRequiredJsonMixin, View):
    def put(self, request):
        # similar to post
        body_str = request.body.decode()
        body_dict = json.loads(body_str)
        email = body_dict.get('email')
        if not email:
            return JsonResponse({'code':400, 'errmsg':'请输入邮箱'})
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            return JsonResponse({'code':400, 'errmsg':'邮箱格式错误'})

        # 保存
        user=request.user
        user.email=email
        user.save()

        # 发送邮件
        token=generic_email_verify_token(request.user.id)
        hyperlink=f"<a href='http://127.0.0.1:8000/emails/verification/?token={token}'> \
        http://127.0.0.1:8000/emails/verification/?token={token}</a>"

        # html_message覆盖message
        subject = '【美多商城】感谢您的使用，请激活邮箱'
        message = None
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        html_message = '<p>请点击以下链接激活账号（有效期为：此邮件发出后的30分钟）</p>' + hyperlink

        from celery_tasks.email.tasks import celery_send_email
        celery_send_email.delay(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            html_message=html_message
        )

        return JsonResponse({'code':0, 'errmsg':'ok'})

class EmailVerifyView(View):
    def put(self, request):
        token=request.GET.get('token')
        print(token)

        if token is None:
            return JsonResponse({'code':400, 'errmsg':'参数缺失'})

        user_id=check_verify_token(token)
        if user_id is None:
            return JsonResponse({'code':400, 'errmsg':'参数错误'})

        user=User.objects.get(id=user_id)
        user.email_active=True
        user.save()

        return JsonResponse({'code':0, 'errmsg':'ok'})







