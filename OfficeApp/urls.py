from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("profile", views.profile_view, name="profile"),
    path("schimba_parola", views.change_password_view, name="schparola"),
    path("logout", views.logout_view, name="logout"),
]