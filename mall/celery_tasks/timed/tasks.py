import os

from django.template import loader

from apps.contents.models import Banner, FlashNew
from apps.goods.utils import get_categories
from celery_tasks.main import app
from mall import settings


@app.task
def generic_meiduo_index():
    try:
        categories = get_categories()
        contents = {}
        contents['banners'] = Banner.objects.filter(status=True).order_by('sequence')
        contents['flash_news'] = FlashNew.objects.filter(status=True).order_by('sequence')

        context = {
            'categories': categories,
            'contents': contents
        }

        # 页面静态化
        index_template = loader.get_template('index.html')
        index_html = index_template.render(context)

        # 创建static目录（如果不存在）
        static_dir = os.path.join(settings.BASE_DIR, 'static')
        os.makedirs(static_dir, exist_ok=True)

        # 写入文件
        file_path = os.path.join(static_dir, 'index.html')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(index_html)

        print("首页静态化完成！")

    except Exception as e:
        print(f"静态化过程中出错: {e}")