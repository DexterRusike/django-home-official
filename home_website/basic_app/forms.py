from django import forms
from django.contrib.auth.models import User
from . import models

class HomeTimesheetForm(forms.ModelForm):
    class Meta():
        model = models.HomeTimesheet
        fields = ('chore_name', 'day')
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = models.UserProfileInfo
        fields = ('profile_pic',)
        
        
