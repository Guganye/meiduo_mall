from collections import OrderedDict

from apps.goods.models import GoodsChannel, SKUSpecification


def get_categories():
    categories = OrderedDict()
    channels = GoodsChannel.objects.order_by('group_id', 'sequence')
    for channel in channels:
        group_id = channel.group_id
        if group_id not in categories:
            categories[group_id] = {'channels': [], 'sub_cats': []}
        cat1 = channel.category
        categories[group_id]['channels'].append({
            'id': cat1.id,
            'name': cat1.name,
            'url': channel.url
        })

        for cat2 in cat1.subs.all():
            cat2.sub_cats=[]
            for cat3 in cat2.subs.all():
                cat2.sub_cats.append(cat3)
            categories[group_id]['sub_cats'].append(cat2)

    return categories

def get_breadcrumb(category):
    dict={
        'cat1':'',
        'cat2':'',
        'cat3':''
    }
    classification=0

    if category.parent is None:
        dict['cat1'] = category.name
        classification=1
    elif category.parent.parent is None:
        dict['cat2'] = category.name
        dict['cat1'] = category.parent.name
        classification=2
    elif category.parent.parent.parent is None:
        dict['cat1'] = category.parent.parent.name
        dict['cat2'] = category.parent.name
        dict['cat3'] = category.name
        classification=3
    else:
        dict['cat1'] = category.parent.parent.parent.name
        dict['cat2'] = category.parent.parent.name
        dict['cat3'] = category.parent.name
        classification=4
    return dict, classification

def get_goods_specs(sku):
    skuspecs=SKUSpecification.objects.filter(sku=sku)
    dict={}
    for skuspec in skuspecs:
        dict[skuspec.option.spec.name]=skuspec.option.value

    return dict