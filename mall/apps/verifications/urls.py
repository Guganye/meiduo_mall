from django.urls import path
from apps.verifications.views import ImageCodeView

urlpatterns = [
    path('image/<code>/', ImageCodeView.as_view(), name='image_codes'),
]