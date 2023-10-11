import re

from django import template

from menu.models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_id = re.findall(r'\d+', context['request'].path)
    menu_items = [item for item in Menu.objects.get(title=menu_name).menu_items.filter(parent=None)]
    active_ips = []
    if not current_id:
        return {'menu_items': menu_items, 'active_ips': active_ips}

    active_ips = [int(active_ip) for active_ip in
                  MenuItem.objects.get(id=current_id[0]).get_parents_ids().split()[::-1]]
    for active_ip in active_ips:
        for index, item in enumerate(menu_items):
            if item.id != active_ip:
                continue
            for child in item.children.all():
                menu_items.insert(index + 1, child)
            break

    return {'menu_items': menu_items, 'active_ips': active_ips}
