# Generated by Django 3.2.6 on 2021-08-31 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_userinfo_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='pfp',
            field=models.ImageField(null=True, upload_to='static/img/{user.username}'),
        ),
    ]
