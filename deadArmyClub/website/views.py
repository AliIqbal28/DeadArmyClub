from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def page2(request):
    render(request, 'page2.html')
