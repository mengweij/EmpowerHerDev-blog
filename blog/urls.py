from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #告诉了 Django，如果有人访问 '' 地址，那么 views.post_list 是这个请求该去到的地方
    #name='post_list' 是 URL 的名字，用来唯一标识对应的 view。 它可以跟 view 的名字一样，也可以完全不一样
    
]