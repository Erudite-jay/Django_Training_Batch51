from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Contact
from .Serializers import ContactSerializer

# Create your views here.

def hello_world(request):
   return HttpResponse("Hello, world! i am backend , first view")

def home_page(request):
   return render(request, 'Auth_app/index.html')

def all_data(request):
   if request.method == 'GET':
      all_contacts = Contact.objects.all()  #queryset
      serializer_data = ContactSerializer(all_contacts, many=True) #serialized data
      return JsonResponse(serializer_data.data,safe=False) 