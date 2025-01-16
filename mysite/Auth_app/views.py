from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
   return HttpResponse("Hello, world! i am backend , first view")

def home_page(request):
   return render(request, 'Auth_app/index.html')