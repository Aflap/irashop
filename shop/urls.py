from django.urls import path
from shop import views
app_name="shop"




urlpatterns = [
       path('',views.allcategories,name="allcat"),
path('allproducts/<p>',views.allproducts,name="allproducts"),
path('detail/<p>',views.detail,name="detail"),
    path('reg', views.register, name="register"),
    path('login', views.user_login, name="login"),
path('logout', views.user_logout, name="logout"),
]
