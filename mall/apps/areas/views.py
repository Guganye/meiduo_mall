from django.core.cache import cache # settings.CACHES.get("default")
# 应用在不经常变动的数据上
from django.http import JsonResponse
from django.views import View

from apps.areas.models import Area


# Create your views here.
class AreaView(View):
    def get(self, request):
        # 有缓存取缓存
        province_list=cache.get('province_list')
        if province_list is None:
            provinces=Area.objects.filter(parent_id = None)

            #QuerySet -> List
            province_list=[]
            for province in provinces:
                print(province.name)
                province_list.append({
                    'id': province.id,
                    'name':province.name,
                })

            # 无缓存查数据库放缓存
            cache.set('province_list', province_list, timeout=24*3600)

        return JsonResponse({'code':0, 'errmsg':'ok', 'province_list':province_list})

class SubAreaView(View):
    def get(self, request, id):
        subarea_list=cache.get(f'subarea:{id}')
        if subarea_list is None:
            area=Area.objects.get(id=id)
            subareas=area.subs.all()
            subarea_list=[]
            for subarea in subareas:
                subarea_list.append({
                    'id': subarea.id,
                    'name':subarea.name,
                })
            cache.set(f'subarea:{id}', subarea_list, timeout=24*3600)

        return JsonResponse({'code':0, 'errmsg':'ok', 'sub_data':{'subs':subarea_list}})

