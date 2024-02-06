from django import template
from django.http import Http404
from django.template import RequestContext
from menu_app.models import MenuCategory

register = template.Library()

@register.inclusion_tag('menu_app/include/menu.html', takes_context=True)
def draw_menu(context=RequestContext, menu_title=''):
    url = context.request.path.replace('/', '')
    menu = MenuCategory.objects.filter(main_menu__title = menu_title).select_related('category')
    found_item_list = [category for category in menu if category.url == url]
    if len(found_item_list) == 0:
        raise Http404
    found_category = found_item_list[0]
    active_categories = found_category.get_three()
    main_categories = [category for category in menu if category.category is None]
    return {'menu': menu, 'active_categories': active_categories, 'main_categories': main_categories, 'found_category': found_category}

@register.inclusion_tag('menu_app/include/menu.html')
def draw_children_menu(menu_item):
    return {'children': menu_item.children.all()}

