from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from .models import Contact
from .Serializers import ContactSerializer
from django.views.decorators.csrf import csrf_exempt

import json
# Create your views here.

def hello_world(request):
   return HttpResponse("Hello, world! i am backend , first view")

def home_page(request):
   return render(request, 'Auth_app/index.html')

@csrf_exempt
def all_data(request):
   if request.method == 'GET':
      all_contacts = Contact.objects.all()  #queryset
      serializer_data = ContactSerializer(all_contacts, many=True) #serialized data
      return JsonResponse(serializer_data.data,safe=False)
   
   if request.method == 'POST':
      input_data= json.loads(request.body)
      serializer = ContactSerializer(data=input_data)

      if serializer.is_valid():
         serializer.save()
         return JsonResponse({
            "success": True,
            "message": "Contact created successfully",
            "data": serializer.data
         })


@csrf_exempt
def single_user_data(request,pk):
   
    if request.method == 'GET':
        try:
            contact = Contact.objects.get(id=pk) #queryset
            serializer = ContactSerializer(contact)    #serialized data
            
            return JsonResponse({
                "success": True,
                "data": serializer.data
            },status=200)
        except Contact.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Contact not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            },status=500)
    
    if request.method == 'PUT':
       try:
            contact = Contact.objects.get(id=pk) #here we are finding user
            input_data= json.loads(request.body)
            serializer = ContactSerializer(contact, data=input_data)

            if serializer.is_valid():
               serializer.save()
               return JsonResponse({
                  "success": True,
                  "message": "Contact updated successfully",
                  "data": serializer.data
               })
       except Contact.DoesNotExist:
           return JsonResponse({
               "success": False,
               "message": "Contact not found"
           },status=404)
       except Exception as e:
           return JsonResponse({
               "success": False,
               "message": str(e)
           },status=500)
    
    if request.method == 'DELETE':
        try:
            contact = Contact.objects.get(id=pk)
            contact.delete()

            return JsonResponse({
                "success": True,
                "message": "Contact deleted successfully"
            })
        except Contact.DoesNotExist:
            return JsonResponse({
                "success": False,
                "message": "Contact not found"
            },status=404)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            },status=500)
        
    if request.method == 'PATCH':
        try:
            single_user = Contact.objects.get(id=pk)
            input_data = json.loads(request.body)

            sd=ContactSerializer(single_user,data=input_data,partial=True)

            if sd.is_valid():
                sd.save()
                return JsonResponse({
                    "success": True,
                    "message": "Contact updated successfully",
                    "data": sd.data
                },status=200)
        except Exception as e:
            return JsonResponse({
                "success": False,
                "message": str(e)
            },status=500)