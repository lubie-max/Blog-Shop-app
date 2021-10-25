from django.contrib import admin
from django.urls import path
from Shop import views

urlpatterns = [
    path('', views.home , name= 'index'),
    path('home/', views.home , name= 'home'),
    path('shopcart/', views.shopcart, name='shopcart'),   
    path('products/', views.products, name='products'),   
    path('item/', views.item, name='item'),   
    path('contact/',views.contact, name='contact'),
    path('about/', views.about, name= 'about'),
    

]