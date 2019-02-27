# Generated by Django 2.1.4 on 2018-12-24 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chuong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chuong', models.CharField(max_length=10, verbose_name='Chương')),
                ('tenchuong', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Tiêu đề chương')),
                ('chuyen', models.TextField(default='', verbose_name='Nội dung')),
                ('ngayup', models.DateTimeField(blank=True, null=True, verbose_name='Ngày upload')),
            ],
            options={
                'verbose_name': 'Chương các Light Novel',
                'verbose_name_plural': 'Chương các Light Novel',
            },
        ),
        migrations.CreateModel(
            name='LightNovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tentruyen', models.CharField(max_length=100, verbose_name='Tên truyện')),
                ('tacgia', models.CharField(max_length=100, verbose_name='Tác giả')),
                ('anh', models.ImageField(upload_to='LightNovelThumbnail', verbose_name='Ảnh')),
                ('gioithieu', models.TextField(blank=True, default='', null=True, verbose_name='Giới thiệu')),
            ],
            options={
                'verbose_name': 'Danh sách Light Novel',
                'verbose_name_plural': 'Danh sách Light Novel',
            },
        ),
        migrations.CreateModel(
            name='TheLoaiLN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=20, verbose_name='Tên thể loại')),
            ],
            options={
                'verbose_name': 'Danh sách thể loại',
                'verbose_name_plural': 'Danh sách thể loại',
            },
        ),
        migrations.AddField(
            model_name='lightnovel',
            name='theloai',
            field=models.ManyToManyField(blank=True, default='', to='lightnovel.TheLoaiLN'),
        ),
        migrations.AddField(
            model_name='chuong',
            name='lightnovel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lightnovel.LightNovel'),
        ),
    ]