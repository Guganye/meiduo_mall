from django.db import models

from utils.models import BaseModel


# Create your models here.
class ContentCategory(BaseModel):
    name = models.CharField(max_length=50)
    key=models.CharField(max_length=50, verbose_name='类别键名')

    class Meta:
        db_table='tb_content_category'
        verbose_name='广告内容类别'
        verbose_name_plural=verbose_name

class Content(BaseModel):
    category = models.ForeignKey(ContentCategory, on_delete=models.PROTECT)
    title=models.CharField(max_length=100)
    url=models.CharField(max_length=300)
    image=models.ImageField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    sequence=models.IntegerField(verbose_name='排序')
    status=models.BooleanField(default=True, verbose_name='是否展示')

    class Meta:
        db_table='tb_content'
        verbose_name='广告内容'
        verbose_name_plural=verbose_name

