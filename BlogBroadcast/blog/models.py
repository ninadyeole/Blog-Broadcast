from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key  = True)
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length = 50)
    views = models.IntegerField(default=0)
    content = models.TextField()
    timestamp = models.DateTimeField(default=now, blank = True)

    def __str__(self):
        return self.title + ' by ' + self.author.username

class blogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return '"' + self.comment[0:18] + '..."' + ' by ' + self.user.username