import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, unique=True)
    email_active = models.BooleanField(default=False)
    default_address = models.ForeignKey('Address', on_delete=models.SET_NULL, related_name='users', null=True, blank=True)

    class Meta:
        db_table = 'tb_users'

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, default='')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addresses')
    receiver = models.CharField(max_length=50)
    province = models.ForeignKey('areas.Area', on_delete=models.CASCADE, related_name='provinces')
    city = models.ForeignKey('areas.Area', on_delete=models.CASCADE, related_name='cities')
    district = models.ForeignKey('areas.Area', on_delete=models.CASCADE, related_name='districts')
    place = models.CharField(max_length=50)
    mobile = models.CharField(max_length=11, verbose_name='手机')
    tel=models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email=models.CharField(max_length=50, null=True, blank=True, default='')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'tb_addresses'
        verbose_name='用户地址'
        verbose_name_plural = '用户地址'
