from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("hello world. you are about")

def contact(request):
    return HttpResponse("hello world. you are at contact")
