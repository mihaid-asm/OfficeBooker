from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from datetime import timedelta, datetime, date
import re
from OfficeBooker.OfficeApp.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    telefon = forms.CharField(required=True)
    data_nastere = forms.DateField(required=True, widget=forms.SelectDateWidget(empty_label="Nothing", years=list(range(1900,date.today().year + 1))))
    cod_postal = forms.IntegerField(required=True)
    adresa = forms.CharField(required=True)
    date = forms.BooleanField(required=True)
    class Meta:
        model = CustomUser
        fields = ("name", "email", "password1", "password2", "telefon", "profile_pic")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.telefon = self.cleaned_data["telefon"]
        user.data_nastere = self.cleaned_data["data_nastere"]
        user.cod_postal = self.cleaned_data["cod_postal"]
        user.adresa = self.cleaned_data["adresa"]
        user.date = self.cleaned_data["date"]
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    ramane_logat = forms.BooleanField(
        required=False,
        initial=False,
        label='Ramaneti logat'
    )
"""    def clean(self):
        cleaned_data = super().clean()
        ramane_logat = self.cleaned_data.get('ramane_logat')
        return cleaned_data"""

class CustomPasswordChangeForm(PasswordChangeForm):
    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        if len(password1) < 8:
            raise forms.ValidationError("Parola trebuie sa aiba macar 8 caractere.")
        return password1