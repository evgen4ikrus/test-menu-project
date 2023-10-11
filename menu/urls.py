from django.urls import path

from .views import MenuItemView, index

urlpatterns = [
    path('', index),
    path('<int:pk>/', MenuItemView.as_view(), name="menu-item-detail"),
]
