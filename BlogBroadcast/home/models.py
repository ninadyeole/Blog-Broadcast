from django.db import models
from django.db.models.deletion import CASCADE
from .storage import OverwriteStorage
import os
from uuid import uuid4
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key  = True)
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 13)
    email = models.EmailField(max_length = 100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True, blank = True)

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email


def path_and_rename(instance, filename):
    upload_to = ''
    ext = filename.split('.')[-1]
    # get filename
    if instance.user.username:
        filename = '{}.{}'.format(instance.user.username, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class userInfo(models.Model):
    sno = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=CASCADE)
    bloglink = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    pfp = models.ImageField(upload_to=path_and_rename, blank= True, null =True)
    location = models.CharField(max_length=80, default="")

    def __str__(self):
        return 'Info on ' + self.user.username