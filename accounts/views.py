from django.shortcuts import render
from .models import *
# Create your views here.

def addedjucation(request):
    return render(request,'accounts/add-edjucation.html',{})


def addexperience(request):
    return render(request,'accounts/add-experience.html',{})


def create(request):
    return render(request,'accounts/create-profile.html',{})


def dashboard(request):
    return render(request,'accounts/dashboard.html',{})


def login_view(request):
    return render(request,'accounts/login.html',{})

def profile(request,pk):
    p=UserProfile.objects.get(pk=pk)
    return render(request,'accounts/profile.html',{'p':p})

def profiles(request):
    return render(request,'accounts/profiles.html',{})


def register(request):
    return render(request,'accounts/register.html',{})


