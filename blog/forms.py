from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #因此所有通过表单传递的数据都在request.POST中
        fields = ('title', 'text',)
        # 只设置两个字段
        # author应该是当前登录的人（你！）然后created_date应该是我们创建文章时自动分配的  