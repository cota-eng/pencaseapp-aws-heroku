# Generated by Django 2.2.8 on 2020-12-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(upload_to='media/blog/%Y/%m/%d', verbose_name='サムネイル'),
        ),
    ]
