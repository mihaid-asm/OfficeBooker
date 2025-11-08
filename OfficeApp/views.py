import numpy as np
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from OfficeBooker.OfficeApp.forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm
from OfficeBooker.OfficeApp.models import CustomUser


# Create your views here.

def index(request):
    return HttpResponse("Primul raspuns")

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            alnum = [chr(i) for i in range(ord('a'), ord('z')+1)] + [chr(i) for i in range(ord('A'), ord('Z')+1)] + [i for i in range(10)]
            anlen = len(alnum)
            code = ""
            leng = np.floor(np.random.rand() * 11 + 15)
            for i in range(leng):
                code += alnum[np.floor(np.random.rand() * anlen)]
            user = CustomUser.objects.get(username=form.cleaned_data['username'])
            user.cod = code
            user.save()
            if len(form.cleaned_data["password"]) < 10:
                messages.warning(request, "Va recomandam o parola cu minim 10 caractere.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
        return redirect('profile')
    else:
        form = CustomAuthenticationForm()
    messages.info(request, "V-ati logat.")
    return render(request, 'login.html', {'form': form})

def profile_view(request):
    messages.debug(request, "Profilul este vizibil.")
    return render(request, 'profile.html')

def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            if len(form.cleaned_data["password"]) < 10:
                messages.warning(request, "Va recomandam o parola cu minim 10 caractere.")
            update_session_auth_hash(request, request.user)
            messages.success(request, 'Parola a fost actualizata')
            return redirect('profile')
        else:
            messages.error(request, 'Exista erori.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    messages.success(request, "Parola schimbata cu succes.")
    return render(request, 'schimba_parola.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "V-ati delogat.")
    return redirect('login')