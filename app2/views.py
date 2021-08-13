from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def app2_hello(request):
    return HttpResponse('This our second view')
