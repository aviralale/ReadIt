# Generated by Django 4.2.2 on 2023-07-09 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='cover_picture',
            field=models.ImageField(default='/user/cover_pic.webp', upload_to='user/'),
        ),
    ]