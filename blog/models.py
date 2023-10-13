from django.db import models
from django.conf import settings

# Create your models here.

#tao bang Post gồm 4 trường
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return self.title


#tao bang Comment gồm 4 trường: post, author, body, date
class Comment(models.Model):
    #field ForeignKey để cho Django xác định đây là khóa ngoại
    #tham số on_delete thuộc loại CASCADE (có nghĩa là khi xóa bài viết thì xóa luôn bình luận),
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name ='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)