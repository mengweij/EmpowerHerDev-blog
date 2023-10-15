from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    #告诉了 Django，如果有人访问 '' 地址，那么 views.post_list 是这个请求该去到的地方
    #name='post_list' 是 URL 的名字，用来唯一标识对应的 view。 它可以跟 view 的名字一样，也可以完全不一样
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    #pk在Django项目中常常用，但是你可以使用你想要的变量（记住：使用小写以及_而不是空格！）
    #注意在升级后的Django URL路由系统中，不再使用正则表达式，而是使用类似<int:pk>这样的路径参数
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]