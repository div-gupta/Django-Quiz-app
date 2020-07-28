from django import forms
from .models import Register

class RegisterUser(forms.ModelForm):
    first_name = forms.CharField(max_length=33,null = True)
    last_name = forms.CharField(max_length=33,null = True)
    birthday = forms.DateField(null = True)
    gender = forms.CharField(max_length=20,null = True)
    username1 = forms.CharField(max_length=33,null = True)
    email = forms.EmailField(max_length=33,null = True)
    password1 = forms.CharField(max_length=33,null = True)
    phone = forms.CharField(max_length=10,null=True)
    qualification = forms.CharField(max_length=40,null=True)
