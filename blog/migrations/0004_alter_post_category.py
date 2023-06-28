# Generated by Django 4.2.2 on 2023-06-27 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('world', 'World'), ('us', 'U.S.'), ('technology', 'Technology'), ('design', 'Design'), ('culture', 'Culture'), ('business', 'Business'), ('politics', 'Politics'), ('opinion', 'Opinion'), ('science', 'Science'), ('health', 'Health'), ('style', 'Style'), ('travel', 'Travel')], max_length=50),
        ),
    ]