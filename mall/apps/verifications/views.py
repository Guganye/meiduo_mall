from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from ronglian_sms_sdk import SmsSDK

from libs.captcha.captcha import captcha


# Create your views here.
class SmsCodeView(View):
    def get(self, request, mobile):
        image_code=request.GET.get('image_code')
        image_code_id=request.GET.get('image_code_id')

        if not all([image_code, image_code_id]):
            return JsonResponse({'code':400, 'errmsg':'参数不全'})

        # 图片验证码
        redis_cli=get_redis_connection('code')
        redis_image_code=redis_cli.get(image_code_id)
        if redis_image_code is None:
            return JsonResponse({'code':400,'errmsg':'图片验证码已过期'})
        if redis_image_code.decode().lower() != image_code.lower():
            return JsonResponse({'code':400, 'errmsg':'图片验证码错误'})

        # 短信验证码
        send_flag=redis_cli.get('send_flag_%s'%mobile)
        if send_flag is not None:
            return JsonResponse({'code':400, 'errmsg':'操作太频繁了'})

        sms_code = '%04d' % random.randint(0,9999)
        # ----------------------------------
        # redis_cli.setex(mobile, 300, sms_code)
        # redis_cli.setex('send_flag_%s' % mobile, 60, 1)
        # 管道技术(性能提升)
        pl = redis_cli.pipeline()
        pl.setex('sms_%s'%mobile, 300, sms_code)
        pl.setex('send_flag_%s'%mobile, 300, 1)
        pl.execute()
        # ----------------------------------
        # https://www.yuntongxun.com/
        # pip install ronglian_sms_sdk
        # 初始化sdk
        sdk=SmsSDK(accId='2c94811c9860a9c4019888893e0d07c3', \
                   accToken='0f251435c33e41fba0de98d07fd09620',\
                   appId='2c94811c9860a9c4019888893fcf07ca')
        # 调用发送短信方法
        sdk.sendMessage(tid='1', mobile='18126106878', datas=(sms_code, '5'))
        return JsonResponse({'code':0, 'errmsg':'ok'})

class ImageCodeView(View):

    def get(self, request, image_code_id):
        captcha = Captcha()
        text, image = captcha.generate_captcha()

        redis_cli = get_redis_connection('code')
        redis_cli.setex(image_code_id, 100, text)

        return HttpResponse(content=image, content_type="image/jpeg")

# -----------------------------

from PIL import Image, ImageDraw, ImageFont
import random
import io
import string

# PILLOW不兼容
class Captcha:
    def __init__(self):
        self.width = 120
        self.height = 40
        self.bg_color = (73, 109, 137)
        self.text_color = (255, 255, 255)
        self.font_size = 24
        self.allowed_chars = string.ascii_uppercase.replace('I', '').replace('O', '') + '23456789'

    def generate_captcha(self):
        """生成验证码（兼容Pillow 9.0+）"""
        # 生成随机文本
        text = ''.join(random.choices(self.allowed_chars, k=4))

        # 创建图片
        img = Image.new('RGB', (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(img)

        # 加载字体
        try:
            font = ImageFont.truetype('arial.ttf', self.font_size)
        except:
            font = ImageFont.load_default()

        # ✅ 关键修复：使用textbbox替代textsize
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # 绘制文本
        x = (self.width - text_width) / 2
        y = (self.height - text_height) / 2
        draw.text((x, y), text, fill=self.text_color, font=font)

        # 添加干扰线
        self._add_noise(draw)

        # 返回结果
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        return text, buf.getvalue()

    def _add_noise(self, draw: ImageDraw.ImageDraw):
        """增强版干扰线生成（带随机颜色和位置）"""
        for _ in range(3):  # 生成3条干扰线
            # 随机起点和终点坐标
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)

            # 随机RGB颜色（较浅色系）
            line_color = (
                random.randint(150, 220),
                random.randint(150, 220),
                random.randint(150, 220)
            )

            # ✅ 调用draw.line()
            draw.line(
                [(x1, y1), (x2, y2)],  # 线段坐标列表
                fill=line_color,  # 线条颜色
                width=1  # 线宽
            )


if __name__ == '__main__':
    sdk = SmsSDK(accId='2c94811c9860a9c4019888893e0d07c3', \
                 accToken='0f251435c33e41fba0de98d07fd09620', \
                 appId='2c94811c9860a9c4019888893fcf07ca')
    # 调用发送短信方法
    sdk.sendMessage(tid='1', mobile='18126106878', datas=(1234,'5'))
