# Generated by Django 2.2.8 on 2020-12-12 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201205_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(default='初期ユーザー', max_length=10, verbose_name='ニックネーム'),
        ),
    ]