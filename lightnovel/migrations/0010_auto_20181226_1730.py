# Generated by Django 2.1.4 on 2018-12-26 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lightnovel', '0009_auto_20181225_2157'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chuong',
            options={'verbose_name': 'Quản lý danh sách các tập truyện CHỮ', 'verbose_name_plural': 'Quản lý danh sách các tập truyện CHỮ'},
        ),
        migrations.AlterModelOptions(
            name='lightnovel',
            options={'verbose_name': 'Quản lý danh sách các truyện CHỮ', 'verbose_name_plural': 'Quản lý danh sách các truyện CHỮ'},
        ),
        migrations.AlterModelOptions(
            name='theloailn',
            options={'verbose_name': 'Quản lý danh sách thể loại', 'verbose_name_plural': 'Quản lý danh sách thể loại'},
        ),
    ]
