from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import Profile


class DateInput(forms.DateInput):
    input_type = 'date'

class ExtendUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username','email','first_name','last_name')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location','birthdate','nik')
        # fields = '__all__'
        widgets = {'birthdate': DateInput()}