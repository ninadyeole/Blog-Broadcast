# Generated by Django 3.2.6 on 2021-08-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='bloglink',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='pfp',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
