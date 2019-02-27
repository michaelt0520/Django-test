from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from lightnovel.models import LightNovel
from audio.models import Audio

from .forms import SignUpForm

def signup(request):
    LN_All = LightNovel.objects.all()
    AU_All = Audio.objects.all()
    
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'LN_All': LN_All, 'AU_All': AU_All})