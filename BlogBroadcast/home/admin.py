from django.contrib import admin
from home.models import Contact, userInfo

admin.site.register((Contact, userInfo))