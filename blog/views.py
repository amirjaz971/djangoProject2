from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    return render(request,'blog/index.html',{})


def post(request):
    return render(request,'blog/post.html',{})


def posts(request):
    return render(request,'blog/posts.html',{})