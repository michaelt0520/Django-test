# Generated by Django 2.1.4 on 2018-12-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lightnovel', '0011_lightnovel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chuong',
            name='tenchuong',
            field=models.CharField(blank=True, default=' ', max_length=50, null=True, verbose_name='Tiêu đề chương'),
        ),
    ]
