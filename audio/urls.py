from django.urls import path
from . import views

app_name = 'audio'

urlpatterns = [
    path('<int:audio_id>/', views.dschuong, name='dschuong'),
    path('the-loai/<int:theloai_id>/', views.TheLoaiTruyen, name='theloaitruyen'),
    path('<int:audio_id>/followau', views.followau, name='au_follow'),
    path('<int:audio_id>/unfollowau', views.unfollowau, name='au_unfollow'),
    path('<int:audio_id>/<int:tap_id>/', views.truyen, name='doctruyen'),
]
