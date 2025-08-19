from django.db import models

# Create your models here.
class Area(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    # 自引用外键关系
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               related_name='subs', null=True, blank=True,
                               verbose_name='上级行政区划')
    # name parent subs
    # province = Area.objects.create(name="河北省")
    # city = Area.objects.create(name="石家庄市", parent=province)
    #
    # province.subs.all()  # 返回 [<Area: 石家庄市>对象...]
    #
    # city.parent  # 返回 <Area: 河北省>对象

    # related_name 默认是关联模型类名小写_set area_set

    class Meta:
        db_table = 'tb_areas'
        verbose_name='省市区'
        verbose_name_plural='省市区'

    def __str__(self):
        return self.name