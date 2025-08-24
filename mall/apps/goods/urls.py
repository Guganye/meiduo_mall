from django.urls import path

from apps.goods.views import IndexView, ListView, DetailView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('list/<int:category_id>/skus', ListView.as_view(), name='list'),
    path('detail/<int:sku_id>/', DetailView.as_view(), name='detail'),
]