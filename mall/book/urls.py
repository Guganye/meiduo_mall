from django.urls import path
from . import views

urlpatterns = [
    path('user/<str:username>', views.set_cookie),
    path('user/', views.get_cookie),
]