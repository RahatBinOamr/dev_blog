from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from user.models import Profile

class RegistrationForm(UserCreationForm): 
    class Meta:
        model=User
        fields =['first_name', 'username', 'email', 'password1','password2']


class UpdateRegisterForm(forms.ModelForm):
    class Meta:
        model= User
        fields =[ 'first_name','username',  'email']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        