from django.urls import path
from . import views

app_name ='lightnovel'

urlpatterns = [
    path('', views.index, name='index'),
    path('lightnovel/results/', views.SearchTruyen, name='danhsachsearch'),
    path('lightnovel/the-loai/<int:theloai_id>', views.TheLoaiTruyen, name='theloaitruyen'),
    path('lightnovel/<int:lightnovel_id>/followln', views.followln, name='ln_follow'),
    path('lightnovel/<int:lightnovel_id>/unfollowln', views.unfollowln, name='ln_unfollow'),
    path('lightnovel/<int:lightnovel_id>/', views.dschuong, name='dschuong'),
    path('lightnovel/<int:lightnovel_id>/<int:chuong_id>/', views.truyen, name='doctruyen'),
]

