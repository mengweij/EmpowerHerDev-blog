from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

#post_list方法接受 request 参数作为输入， 并 return （返回）用 render 方法渲染模板 blog/post_list.html
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #返回request, template地址，{}中则是template需要的东西
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})