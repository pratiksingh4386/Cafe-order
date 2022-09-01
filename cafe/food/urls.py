from . import views
from django.urls import path
urlpatterns = [
    # path('',views.menu,name='menu'),
    path('menu/',views.menu,name='menu'),
    path('details/<int:id>/',views.details,name='details'),
    path('add_to_cart',views.add_to_cart, name="add_to_cart"),
    path('cart/',views.cart, name="cart"),
    path('delete_cart_items/<str:id>',views.delete_cart_items, name="delete_cart_items"),
    path('check_out/',views.check_out, name="check_out"),
    path('place_order/',views.place_order, name="place_order"),
    path('order/',views.order, name="order"),
    path('search/',views.search, name="search"),
]