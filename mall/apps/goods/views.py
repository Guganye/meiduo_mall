import os

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.http import JsonResponse
from django.template import loader
from django.views import View
from django.views.static import serve

from apps.contents.detail import generic_goods_detail
from apps.contents.models import Banner, FlashNew
from apps.goods.models import GoodsCategory, SKU, SPU
from apps.goods.utils import get_categories, get_breadcrumb
from celery_tasks.timed.tasks import generic_meiduo_index
from mall import settings


# Create your views here.
class IndexView(View):
    def get(self, request):
        file_path = os.path.join(settings.BASE_DIR, 'static')
        try:
            response=serve(request, 'index.html', document_root=file_path)
        except FileNotFoundError:
            response = JsonResponse({'code': 400, 'errmsg': '页面尚未静态化'})
        return response


class ListView(View):
    def get(self, request, category_id):
        page=request.GET.get('page') # 第几页
        page_size=request.GET.get('page_size') # 每页多少条数据
        ordering=request.GET.get('ordering') # 排序
        try:
            category=GoodsCategory.objects.get(id=category_id)
        except GoodsCategory.DoesNotExist:
            return JsonResponse({'code':400,'error':'category does not exist'})
        breadcrumb, classification=get_breadcrumb(category)
        if classification == 1:
            spus = SPU.objects.filter(category1=category)
        elif classification == 2:
            spus = SPU.objects.filter(category2=category)
        elif classification == 3:
            spus = SPU.objects.filter(category3=category)
        else:
            spus = SPU.objects.filter(category=category)


        sku_ids = []
        for spu in spus:
            spu_skus = SKU.objects.filter(Q(spu=spu) & Q(is_launched=True))
            sku_ids.extend([sku.id for sku in spu_skus])

        skus = SKU.objects.filter(id__in=sku_ids).order_by(ordering)

        # 分页
        paginator=Paginator(skus, page_size)
        page_skus=paginator.page(page)

        sku_list=[]
        for sku in page_skus.object_list:
            sku_list.append({
                'id': sku.id,
                'name': sku.name,
                'price': sku.price,
                'default_image_url': sku.default_image.image.url, # FileField类的url方法
            })

        total_num=paginator.num_pages

        return JsonResponse({'code':0, 'errmsg':'ok', 'breadcrumb':breadcrumb
                             ,'list':sku_list, 'count':total_num})


class DetailView(View):
    def get(self, request, sku_id):
        sku=SKU.objects.filter(Q(id=sku_id) & Q(is_launched=True))
        if sku is None:
            return JsonResponse({'code':400,'errmsg':'商品不存在或未上架'})

        file_path = os.path.join(settings.BASE_DIR, 'static')
        try:
            response=serve(request, f'detail_{sku_id}.html', document_root=file_path)
        except FileNotFoundError:
            response=JsonResponse({'code':400,'errmsg':'页面尚未静态化'})
        return response
