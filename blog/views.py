from django.shortcuts import render

#post_list方法接受 request 参数作为输入， 并 return （返回）用 render 方法渲染模板 blog/post_list.html
def post_list(request):
    return render(request, 'blog/post_list.html', {})

