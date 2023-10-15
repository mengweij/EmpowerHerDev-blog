from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # models.Model表明Post是一个Django模型，所以Django知道它应该被保存在数据库中

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #指向另一个模型的链接
    title = models.CharField(max_length=200) #有限字符来定义的文本
    text = models.TextField() #无限字符
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

# comment blog model
class Comment(models.Model):
    # 一个外键字段，关联到Post模型
    # on_delete=models.CASCADE参数表示当关联的博客文章被删除时，与之关联的评论也会被删除。
    # related_name='comments'参数定义了在Post模型中使用的反向关系名称，这意味着post.comments就是评论对象
    # 可以通过post.comments.all()来获取某篇博客文章的评论
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False) #用于标记评论是否得到批准，默认F

    #用于批准评论的方法
    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.text