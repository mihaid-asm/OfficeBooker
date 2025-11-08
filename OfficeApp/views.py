from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
# We only need PasswordChangeForm from here
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#
# THIS IS THE CORRECTED IMPORT
#
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Create your views here.
def index(request):
    return render(request, 'OfficeApp/index.html')

def register_view(request):
    if request.method == "POST":
        # Use the correct Custom form
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('index') # Or profile
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        # Use the correct Custom form
        form = CustomUserCreationForm()
    return render(request, "OfficeApp/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        # Use the correct Custom form
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.info(request, f"You are now logged in as {user.email}.")
            return redirect('index') # Or profile
        else:
            messages.error(request, "Invalid email or password.")
    else:
        # Use the correct Custom form
        form = CustomAuthenticationForm()
    return render(request, "OfficeApp/login.html", {"form": form})

@login_required
def profile_view(request):
    return render(request, 'OfficeApp/profile.html')

@login_required
def change_password_view(request):
    if request.method == "POST":
        #
        # THIS NOW USES THE CORRECT BUILT-IN FORM
        #
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        #
        # THIS NOW USES THE CORRECT BUILT-IN FORM
        #
        form = PasswordChangeForm(request.user)
    return render(request, 'OfficeApp/change_password.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('index')