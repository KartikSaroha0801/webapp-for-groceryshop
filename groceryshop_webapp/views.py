from django.http import HttpResponse
from django.shortcuts import render
from requests import request

def homePage(request):
    return render(request, "homepage.html")

def checkout(request):
    return render(request, "checkout.html")

