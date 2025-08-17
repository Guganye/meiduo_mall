from django.urls import path
from apps.users.views import RegisterView, LoginView, LogoutView, CenterView, EmailView, EmailVerifyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('center/', CenterView.as_view(), name='center'),
    path('emails/', EmailView.as_view(), name='emails'),
    path('emails/verification/', EmailVerifyView.as_view(), name='emails_verification'),
]