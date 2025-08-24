from django.core.exceptions import ValidationError
from django.db import models

from utils.models import BaseModel


# Create your models here.
# spu（标准产品单位）是商品信息聚合的最小单位，是一组标准化信息的集合--------一类产品
# sku（库存量单位）是库存进出计量的单位，是物理上不可分割的最小库存单位------一款产品
class GoodsCategory(BaseModel):
    name=models.CharField(max_length=10)
    parent=models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='subs')

    class Meta:
        db_table = 'tb_goods_category'
        verbose_name='商品类别',
        verbose_name_plural=verbose_name
    # 三级分类结构
    # 手机数码 (一级分类)
    # └── 手机通讯 (二级分类)
    #     └── 智能手机 (三级分类)

class GoodsChannelGroup(BaseModel):
    name=models.CharField(max_length=10)

    class Meta:
        db_table = 'tb_channel_group'
        verbose_name='商品频道组'
        verbose_name_plural=verbose_name

#  多对多
class GoodsChannel(BaseModel):
    group=models.ForeignKey('GoodsChannelGroup', on_delete=models.CASCADE)
    category=models.ForeignKey('GoodsCategory', on_delete=models.CASCADE)
    url=models.CharField(max_length=200, verbose_name='频道页面链接') # 也可以当作是一级类别链接，为什么呢，因为group只装一级标题
    sequence=models.IntegerField(verbose_name='组内顺序')

    class Meta:
        db_table = 'tb_goods_channel'
        verbose_name='商品频道'
        verbose_name_plural=verbose_name
    # 中间表
    # 首页展示的频道
    # "热门推荐"频道组
    # └── "手机数码"频道 → 链接到手机数码分类页面

class Brand(BaseModel):
    name=models.CharField(max_length=20)
    logo=models.ImageField(verbose_name='logo图片')
    first_letter=models.CharField(max_length=1, verbose_name='品牌首字母')

    class Meta:
        db_table = 'tb_brand'
        verbose_name='品牌'
        verbose_name_plural=verbose_name
    # name logo first_letter

class SPU(BaseModel):
    name=models.CharField(max_length=50)
    brand=models.ForeignKey('Brand', on_delete=models.PROTECT)
    category1=models.ForeignKey('GoodsCategory', on_delete=models.PROTECT, related_name='cat1_spu', verbose_name='从属类别1')
    category2=models.ForeignKey('GoodsCategory', on_delete=models.PROTECT, related_name='cat2_spu', verbose_name='从属类别2')
    category3=models.ForeignKey('GoodsCategory', on_delete=models.PROTECT, related_name='cat3_spu', verbose_name='从属类别3')
    category=models.ForeignKey('GoodsCategory', on_delete=models.PROTECT, related_name='cat', verbose_name='类别')
    sales=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    desc_detail=models.TextField(default='', verbose_name='详细介绍')
    desc_pack=models.TextField(default='', verbose_name='包装信息')
    desc_service=models.TextField(default='', verbose_name='售后服务')

    class Meta:
        db_table = 'tb_spu'
        verbose_name='商品spu'
        verbose_name_plural=verbose_name
    # spu 一类产品

class SKU(BaseModel):
    name=models.CharField(max_length=50)
    caption=models.CharField(max_length=100, verbose_name='副标题')
    url=models.CharField(max_length=200, default='',verbose_name='商品链接')
    spu=models.ForeignKey('SPU', on_delete=models.CASCADE, verbose_name='类别')
    price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='单价')
    cost_price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='进价')
    market_price=models.DecimalField(max_digits=10, decimal_places=2, verbose_name='市场价')
    stock=models.IntegerField(default=0, verbose_name='库存')
    sales=models.IntegerField(default=0)
    comments=models.IntegerField(default=0)
    is_launched=models.BooleanField(default=True, verbose_name='是否上架销售')
    default_image = models.ForeignKey('SKUImage',on_delete=models.SET_NULL,null=True,blank=True,related_name='default')
    class Meta:
        db_table = 'tb_sku'
        verbose_name='商品sku'
        verbose_name_plural=verbose_name
    # sku 一款产品

class SKUImage(BaseModel):
    sku=models.ForeignKey('SKU', on_delete=models.CASCADE, related_name='images')
    image=models.ImageField()

    class Meta:
        db_table = 'tb_sku_image'
        verbose_name='sku图片'
        verbose_name_plural=verbose_name

class SPUSpecification(BaseModel):
    spu=models.ForeignKey('SPU', on_delete=models.CASCADE, related_name='specs', verbose_name='商品spu')
    name=models.CharField(max_length=20)

    class Meta:
        db_table = 'tb_spu_specification'
        verbose_name='商品spu规格'
        verbose_name_plural=verbose_name

class SpecificationOption(BaseModel):
    spec = models.ForeignKey('SPUSpecification', related_name='options', on_delete=models.CASCADE)
    value=models.CharField(max_length=20, verbose_name='选项值')

    class Meta:
        db_table = 'tb_specification_option'
        verbose_name = '规格选项'
        verbose_name_plural = verbose_name
    # spec value
    # iPhone 15 的规格
    # 颜色规格 = SPUSpecification(spu=iPhone15_SPU, name="颜色")
    # 内存规格 = SPUSpecification(spu=iPhone15_SPU, name="内存")
    #
    # 规格的具体选项
    # 黑色 = SpecificationOption(spec=颜色规格, value="黑色")
    # 蓝色 = SpecificationOption(spec=颜色规格, value="蓝色")
    # 128GB = SpecificationOption(spec=内存规格, value="128GB")
    # 256GB = SpecificationOption(spec=内存规格, value="256GB")

class SKUSpecification(BaseModel):
    sku=models.ForeignKey('SKU', on_delete=models.CASCADE, related_name='specs')
    option=models.ForeignKey('SpecificationOption', on_delete=models.PROTECT)

    class Meta:
        db_table = 'tb_sku_specification'
        verbose_name='sku规格'
        verbose_name_plural=verbose_name





