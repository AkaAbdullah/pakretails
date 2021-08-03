from .models import Profile
from django.db import models
from django.forms import fields, widgets
from django import forms
from .models import Profile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields=['firstname','lastname','email','phone_no','address','shipping_address']
        widgets={
            'name':forms.TextInput(attrs={'class':'input'}),
            'firstname':forms.TextInput(attrs={'class':'input'}),
            'lastname':forms.TextInput(attrs={'class':'input'}),
            'email':forms.EmailInput(attrs={'class':'input'}),
            'phone_no':forms.TextInput(attrs={'class':'input'}),
            'address':forms.TextInput(attrs={'class':'input'}),
            'shipping_address':forms.TextInput(attrs={'class':'input'}),

        }