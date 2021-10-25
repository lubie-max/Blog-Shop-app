from django.contrib import admin
from django.urls import path
from ShopBlog import views

urlpatterns = [
    path("blog/", views.blog, name="blog"),
    path("blog/blogpost/<str:slug>", views.blogpost, name="blogpost"),
    path("blogger/", views.blogger, name='blogger'),
    path('aboutblog',views.aboutblog, name='aboutblog' ),
]