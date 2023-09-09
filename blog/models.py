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