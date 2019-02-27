from django.http import HttpResponse
from .models import LightNovel, Chuong, TheLoaiLN
from audio.models import Audio, Tap, TheLoaiAU
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from itertools import chain
import random

# Create your views here.
def index(request):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    LN_MoiDang = LightNovel.objects.all().order_by('-ngayup')[:9]
    LN_MoiCapNhat = Chuong.objects.all().values('lightnovel', 'lightnovel__id').annotate(last_ngayup=Max('ngayup')).order_by('-last_ngayup')[:9]
    LN_DaHoanThanh = LightNovel.objects.filter(dahoanthanh=True)[:9]

    AU_MoiDang = Audio.objects.all().order_by('-ngayup')[:9]
    AU_MoiCapNhat = Tap.objects.all().values('audio', 'audio__id').annotate(last_ngayup=Max('ngayup')).order_by('-last_ngayup')[:9] 
    AU_DaHoanThanh = Audio.objects.filter(dahoanthanh=True)[:9]

    all_theloaiLN = TheLoaiLN.objects.all()
    all_theloaiAU = TheLoaiAU.objects.all()
    
    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'LN_MoiDang': LN_MoiDang,
        'LN_MoiCapNhat': LN_MoiCapNhat,
        'LN_DaHoanThanh': LN_DaHoanThanh,
        'AU_MoiDang': AU_MoiDang,
        'AU_MoiCapNhat': AU_MoiCapNhat,
        'AU_DaHoanThanh': AU_DaHoanThanh,
        'all_theloaiLN': all_theloaiLN,
        'all_theloaiAU': all_theloaiAU,
        }
    return render(request, 'index.html', context)

def dschuong(request, lightnovel_id):
    truyen = get_object_or_404(LightNovel, id=lightnovel_id)
    all_chuongs = Chuong.objects.all().filter(lightnovel=truyen)

    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    flag = False
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    for tk in truyen.user.all():
        if tk.username == username:
            flag = True

    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'all_chuongs': all_chuongs,
        'truyen': truyen,
        'flag': flag,
    }
    return render(request, 'basedschuong.html', context)

def truyen(request, lightnovel_id, chuong_id):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    truyen = get_object_or_404(LightNovel, id=lightnovel_id)
    chuong = get_object_or_404(Chuong, id=chuong_id)

    dschuong = Chuong.objects.filter(lightnovel=truyen)
    
    lenght = len(dschuong)
    chuong_tieptheo = chuong_truoc = None

    for index, obj in enumerate(dschuong):
        if obj == chuong:
            if index > 0:
                chuong_truoc = dschuong[index - 1]
            if index < (lenght - 1):
                chuong_tieptheo = dschuong[index + 1]


    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'truyen': truyen,
        'chuong': chuong,
        'chuong_truoc': chuong_truoc,
        'chuong_tieptheo': chuong_tieptheo,
    }
    return render(request, 'basetruyen.html', context)


def SearchTruyen(request):
    query = request.GET.get('q')
    text= 'Tìm kiếm: ' + query

    result = None
    if query != '':
        result1 = LightNovel.objects.filter(tentruyen__contains=query)
        result2 = Audio.objects.filter(tentruyen__contains=query)
        result3 = LightNovel.objects.filter(tacgia__contains=query)
        result4 = Audio.objects.filter(tacgia__contains=query)
        result = chain(result1, result2, result3, result4)
    
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'text': text,
        'result': result,
    }
    return render(request, 'searchform.html', context)

def TheLoaiTruyen(request, theloai_id):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    truyen = LightNovel.objects.filter(theloai__in=[theloai_id])
    text = 'Thể loại: ' + TheLoaiLN.objects.get(id=theloai_id).ten
    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'result': truyen,
        'text' : text,
    }
    return render(request, 'searchform.html', context)

def followln(request,lightnovel_id):
    user = request.user
    ln = LightNovel.objects.get(id=lightnovel_id)

    ln.user.add(user)
    ln.save()
    return redirect(request.META['HTTP_REFERER'])

def unfollowln(request,lightnovel_id):
    user = request.user
    ln = LightNovel.objects.get(id=lightnovel_id)

    ln.user.remove(user)
    ln.save()
    return redirect(request.META['HTTP_REFERER'])
