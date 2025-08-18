from django.http import JsonResponse
from django.views import View

from apps.areas.models import Area


# Create your views here.
class AreaView(View):
    def get(self, request):
        provinces=Area.objects.filter(parent=None)

        #QuerySet -> List
        province_list=[]
        for province in provinces:
            province_list.append({
                'id': province.id,
                'name':province.name,
            })

        return JsonResponse({'code':0, 'errmsg':'ok', 'province_list':province_list})

class SubAreaView(View):
    def get(self, request, id):
        area=Area.objects.get(id=id)
        subareas=area.subs.all()
        subarea_list=[]
        for subarea in subareas:
            subarea_list.append({
                'id': subarea.id,
                'name':subarea.name,
            })
        return JsonResponse({'code':0, 'errmsg':'ok', 'sub_data':{'subs':subarea_list}})

