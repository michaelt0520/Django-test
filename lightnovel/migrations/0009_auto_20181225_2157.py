# Generated by Django 2.1.4 on 2018-12-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightnovel', '0008_auto_20181225_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chuong',
            name='ngayup',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Ngày upload'),
        ),
        migrations.AlterField(
            model_name='lightnovel',
            name='ngayup',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Ngày upload'),
        ),
    ]
