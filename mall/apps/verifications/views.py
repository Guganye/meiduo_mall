from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django_redis import get_redis_connection
from libs.captcha.captcha import captcha


# Create your views here.

class ImageCodeView(View):

    def get(self, request, code):
        captcha = Captcha()
        text, image = captcha.generate_captcha()

        redis_cli = get_redis_connection('code')
        redis_cli.setex(code, 100, text)

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

