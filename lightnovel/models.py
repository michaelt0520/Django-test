from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class TheLoaiLN(models.Model):
    ten = models.CharField(max_length=20, verbose_name='Tên thể loại')

    def __str__(self):
        return self.ten

    class Meta:
        verbose_name = 'Quản lý danh sách thể loại'
        verbose_name_plural = 'Quản lý danh sách thể loại'

class LightNovel(models.Model):
    tentruyen = models.CharField(max_length=100, verbose_name='Tên truyện')
    tacgia = models.CharField(max_length=100, verbose_name='Tác giả')
    theloai = models.ManyToManyField(TheLoaiLN, blank=True, default='')
    anh = models.ImageField(upload_to='LightNovelThumbnail', verbose_name='Ảnh')
    gioithieu = models.TextField(null=True, default='', blank=True, verbose_name='Giới thiệu')
    dahoanthanh = models.BooleanField(default=False, verbose_name='Check vào nếu bộ truyện này đã hoàn thành')
    ngayup = models.DateTimeField(null=True, blank=False, auto_now_add=True, verbose_name='Ngày upload')
    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.tentruyen + ' - ' + self.tacgia

    def get_tentruyen(self):
        return self.tentruyen

    class Meta:
        verbose_name = 'Quản lý danh sách các truyện CHỮ'
        verbose_name_plural = 'Quản lý danh sách các truyện CHỮ'

class Chuong(models.Model):
    lightnovel = models.ForeignKey(LightNovel, on_delete=models.CASCADE, related_name='lightnovel')
    chuong = models.CharField(max_length=10, verbose_name='Chương')
    tenchuong = models.CharField(max_length=50, default='', blank=True, verbose_name='Tiêu đề chương')
    chuyen = models.TextField(default='', verbose_name='Nội dung')
    ngayup = models.DateTimeField(null=True, blank=False, auto_now_add=True, verbose_name='Ngày upload')

    def __str__(self):
        return self.lightnovel.get_tentruyen() + ' - ' + self.chuong
    
    class Meta:
        verbose_name = 'Quản lý danh sách các tập truyện CHỮ'
        verbose_name_plural = 'Quản lý danh sách các tập truyện CHỮ'
