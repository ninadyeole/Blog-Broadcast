# Generated by Django 3.2.6 on 2021-08-30 16:32

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blog_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=30, verbose_name=django.contrib.auth.models.User),
        ),
    ]
