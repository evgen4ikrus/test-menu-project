from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class PositionAdmin(admin.ModelAdmin):
    pass


@admin.register(MenuItem)
class PositionAdmin(admin.ModelAdmin):
    pass
