from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1_fst(request):
    return HttpResponse('This is our first view')