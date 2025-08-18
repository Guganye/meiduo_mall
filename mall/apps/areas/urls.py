from django.urls import path
from apps.areas.views import AreaView, SubAreaView

urlpatterns = [
    path('areas/', AreaView.as_view(), name='area'),
    path('areas/<int:id>/', SubAreaView.as_view(), name='subarea'),
]