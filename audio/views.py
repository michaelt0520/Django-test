from django.shortcuts import render, redirect, get_object_or_404
from .models import Audio, Tap, TheLoaiAU
from django.apps import apps

LightNovel = apps.get_model('lightnovel', 'LightNovel')

# Create your views here.
def dschuong(request, audio_id):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    audio = get_object_or_404(Audio, id=audio_id)
    all_taps = Tap.objects.all().filter(audio=audio)

    flag = False
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    for tk in audio.user.all():
        if tk.username == username:
            flag = True

    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'all_taps': all_taps,
        'audio': audio,
        'flag': flag,
    }
    return render(request, 'basedstap.html', context)

def truyen(request, audio_id, tap_id):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    audio = get_object_or_404(Audio, id=audio_id)
    tap = get_object_or_404(Tap, id=tap_id)

    dstap = Tap.objects.filter(audio=audio)

    lenght = len(dstap)
    tap_tieptheo = tap_truoc = None

    for index, obj in enumerate(dstap):
        if obj == tap:
            if index > 0:
                tap_truoc = dstap[index - 1]
            if index < (lenght - 1):
                tap_tieptheo = dstap[index + 1]

    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'audio': audio,
        'tap': tap,
        'tap_truoc': tap_truoc,
        'tap_tieptheo': tap_tieptheo,
    }
    return render(request, 'basetap.html', context)

def TheLoaiTruyen(request, theloai_id):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()

    audio = Audio.objects.filter(theloai__in=[theloai_id])
    text = 'Thể loại: ' + TheLoaiAU.objects.get(id=theloai_id).ten
    context = {
        'LN_All': LN_All,
        'AU_All': AU_All,
        'result': audio,
        'text' : text,
    }
    return render(request, 'searchform1.html', context)


def followau(request,audio_id):
    user = request.user
    au = Audio.objects.get(id=audio_id)

    au.user.add(user)
    au.save()
    return redirect(request.META['HTTP_REFERER'])

def unfollowau(request,audio_id):
    user = request.user
    au = Audio.objects.get(id=audio_id)

    au.user.remove(user)
    au.save()
    return redirect(request.META['HTTP_REFERER'])