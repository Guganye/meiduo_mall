#!/usr/bin/env python

# django环境下能单独运行的脚本配置
# ----------------------
import os
import django
import sys
# 将上一级目录(../)添加到python的模块搜索路径的最前面
sys.path.insert(0, '../../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mall.settings")
django.setup()
# ----------------------

from django.template import loader
from apps.goods.models import SKU
from apps.goods.utils import get_categories, get_breadcrumb, get_goods_specs
from mall import settings
def generic_goods_detail(sku):
    try:
        breadcrumb, _=get_breadcrumb(sku.spu.category)
        goods_specs=get_goods_specs(sku)

        context={
            'breadcrumb':breadcrumb,
            'goods_specs':goods_specs,
        }

        detail_template=loader.get_template('detail.html')
        detail_html=detail_template.render(context)

        static_dir = os.path.join(settings.BASE_DIR, 'static')
        os.makedirs(static_dir, exist_ok=True)

        file_path = os.path.join(static_dir, f'detail_{sku.id}.html')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(detail_html)

    except Exception as e:
        print(f"详细页_{sku.id}静态化出错:{e}")


if __name__ == '__main__':
    skus=SKU.objects.all()
    for sku in skus:
        generic_goods_detail(sku)

# 详细页 应该在上线的时候 统一都生成一遍