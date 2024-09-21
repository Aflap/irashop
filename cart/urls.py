from django.contrib import admin
from django.urls import path
from cart import views
app_name="cart"
urlpatterns = [
     path('addtocart/<p>',views.add_to_cart,name="addtocart"),
     path('cartview',views.cartview,name="cartview"),
path('cart_remove/<p>',views.cart_remove,name="cart_remove"),
path('full_remove/<p>',views.full_remove,name="full_remove"),
path('orderform',views.orderform,name="orderform"),
path('orderview',views.orderview,name="orderview"),

]