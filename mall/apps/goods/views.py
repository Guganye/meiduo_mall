from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from apps.contents.models import Banner, FlashNew
from apps.goods.utils import get_categories


# Create your views here.
class IndexView(View):
    def get(self, request):
        categories=get_categories()
        contents={}
        contents['banners']=Banner.objects.filter(status=True).order_by('sequence')
        contents['flash_news']=FlashNew.objects.filter(status=True).order_by('sequence')
        context={
            'categories': categories,
            'contents': contents
        }

        return render(request, 'index.html', context)
