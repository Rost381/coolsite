from django import template
from django.http import Http404

from women.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}

@register.simple_tag()
def show_womens(cat_id=None):
    if not cat_id:
        return Women.objects.all()
    else:
        posts = Women.objects.filter(cat_id=cat_id)
        if len(posts) == 0:
            raise Http404()
        return posts
