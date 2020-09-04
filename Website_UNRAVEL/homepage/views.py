from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import SiteContent

def home(request):

    return render(request, "home.html")

def about_us(request):
    return render(request, "about_us.html")

def suggessions(request):
    return render(request, 'suggession_form.html')
    