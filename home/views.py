from django.shortcuts import render, HttpResponse
from django.template import RequestContext

def home(request):
     return render(request, 'home/login.html')
