from django.shortcuts import render
from django.views.generic import DetailView

from .models import MenuItem


def index(request):
    return render(request, 'index.html')


class MenuItemView(DetailView):
    model = MenuItem
    template_name = 'menu_item_detail.html'
    context_object_name = 'menu_item'
