from django.contrib import admin
from blog.models import Blog, blogComment
# Register your models here.

admin.site.register((Blog, blogComment))