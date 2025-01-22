from django.http import JsonResponse
from django.shortcuts import render
from .forms import FileUploadFormClass
from . models import FileUpload
# Create your views here.

def file_upload_form(request):

    if request.method == 'GET':
       form=FileUploadFormClass()

    if request.method == 'POST':
       print(request)
       form=FileUploadFormClass(request.POST, request.FILES)
       print(form)

       if form.is_valid():
        #   record=FileUpload(name=form.cleaned_data["name"], file=form.cleaned_data["file"])
        #   record.save()
           form.save()
        

           return JsonResponse({
             "success":True,
          },status=201)
       
  

    return render(request, 'Form_app/file_upload_form.html', {'form': form})

