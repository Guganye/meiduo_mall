from django.db import models

from utils.models import BaseModel
from apps.goods.models import SKU, SKUImage


# Create your models here.

class Banner(BaseModel):
    image=models.ForeignKey(SKUImage, on_delete=models.PROTECT)
    description=models.TextField(blank=True, null=True)
    sequence=models.IntegerField(default=0, verbose_name='排序')
    status = models.BooleanField(default=True, verbose_name='是否展示')
    class Meta:
        db_table='tb_banner'
        verbose_name='轮播图'
        verbose_name_plural=verbose_name


class FlashNew(BaseModel):
    sku=models.ForeignKey(SKU, on_delete=models.CASCADE)
    content=models.CharField(max_length=200)
    sequence=models.IntegerField(default=0)
    status = models.BooleanField(default=True, verbose_name='是否展示')

    class Meta:
        db_table = 'tb_flash_new'
        verbose_name='快讯'
        verbose_name_plural=verbose_name