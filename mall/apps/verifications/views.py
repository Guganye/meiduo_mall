from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection


# Create your views here.

class ImageCodeView(View):

    def get(self, request, code):
        text, image = captcha.generate_captcha()

        redis_cli = get_redis_connection('code')
        redis_cli.setex(code, 100, text)

        return HttpResponse(image)

