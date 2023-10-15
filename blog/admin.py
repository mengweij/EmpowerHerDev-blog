from django.contrib import admin
from .models import Post, Comment

# 让我们的模型在admin页面上可见
admin.site.register(Post)
admin.site.register(Comment)