from django.urls import path
from apps.areas.views import AreaView

urlpatterns = [
    path('', AreaView.as_view(), name='area'),
]