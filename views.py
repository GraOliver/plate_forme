from django.shortcuts import render,get_list_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *
# Create your views here.

def Accueil (request):
    context ={
        "religion":Religion.objects.all(),
        "communaute":Communaute.objects.all(),
        "message":"Bien venue dans mon programme"
    }
    return render(request,"app/index.html",context)

def page(request):
    return render(request,"app/accueil.html")