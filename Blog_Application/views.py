from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<h1>About us</h1>')

def contact(request):
    return HttpResponse('<h1>contact us</h1>')

