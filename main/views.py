from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from .form import UserProfileForm, ExtendUserCreationForm
from .models import Profile
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required



def index(request):
    if(request.user.is_authenticated):
        variable = request.user.username
        # print(request.user.profile.birthdate)
        response = {'username' : variable}
        return render(request,'home.html',response)
    return render(request,'index.html')


def signup(request):

    form_user = ExtendUserCreationForm(request.POST or None)
    form_extention = UserProfileForm(request.POST or None)
    context = {'form': form_user, 'form_extention': form_extention}
    print(form_user.is_valid())
    print(form_extention.is_valid())

    if(request.method == "POST"):
        if(form_user.is_valid() and form_extention.is_valid()):
            user = form_user.save()
            profile = form_extention.save(commit=False)
       
            username = form_user.cleaned_data.get('username')
            email = form_user.cleaned_data.get('email')
            first_name = form_user.cleaned_data.get('first_name')
            last_name = form_user.cleaned_data.get('last_name')
            password = form_user.cleaned_data.get('password1')
            password_confirm = form_user.cleaned_data.get('password2')
            location = form_extention.cleaned_data.get('location')
            birthdate = form_extention.cleaned_data.get('birthdate')
            nik = form_extention.cleaned_data.get('nik')
   
            profile.user = user
            profile.save()
    
            user = authenticate(request, username = username, password = password)
            messages.success(request, "Your Account has been seccessfuly created!")  
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html', context)

def signin(request):
        
    if(request.method == "POST"):
        username_input = request.POST['username']
        password_input = request.POST['password']

        user = authenticate(request, username = username_input, password = password_input)
        if(user is None):
            print("jiah salah")
        else:
            login(request, user)
            return redirect('home') #nanti kita masukin home
    return render(request,"signin.html")


def signout(request):
    logout(request)
    return redirect("home")

@csrf_exempt
def flutter(request):
    data = serializers.serialize('json', User.objects.all())
    return HttpResponse(data, content_type = "application/json")