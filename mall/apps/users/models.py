import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    mobile = models.CharField(max_length=11, unique=True)
    email_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'tb_users'