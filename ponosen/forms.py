# -*- coding: utf-8 -*-
from django.forms import ModelForm, Form
from django import forms
from django.core.exceptions import ValidationError


class PasswordRecoverForm(Form):
    password = forms.CharField(label="Geslo*", widget=forms.PasswordInput())
    confirm_password = forms.CharField(label="Ponovi geslo*", widget=forms.PasswordInput())

    def clean(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise ValidationError({'confirm_password': "Gesla nista enaka."})
        if len(password) < 5 or len(password) > 10:
            raise ValidationError({'password': "Geslo mora vsebovati vsaj 5 znakov."})
        return {"password": password}