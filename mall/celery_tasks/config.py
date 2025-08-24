from apps.goods.utils import get_categories, get_breadcrumb


def generic_detail_html(sku):
    categories=get_categories()
    breadcrumb=get_breadcrumb(sku.category)
    goods_specs=get_goods_specs(sku)