import numpy as np
from django.contrib import messages
from django.contrib.auth import login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from OfficeBooker.OfficeApp.forms import CustomUserCreationForm, CustomAuthenticationForm, CustomPasswordChangeForm
from OfficeBooker.OfficeApp.models import CustomUser


# Create your views here.

def index(request):
    return HttpResponse("Primul raspuns")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:

        form = CustomUserCreationForm()
    return render(request, "users/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, "users/login.html", {"form": form})

def profile_view(request):
    messages.debug(request, "Profilul este vizibil.")
    return render(request, 'profile.html')


@login_required
def change_password_view(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # BUG FIX: Call form.save() to save the new password
            user = form.save()

            # BUG FIX: Update the session to prevent logout
            update_session_auth_hash(request, user)

            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "V-ati delogat.")
    return redirect('login')