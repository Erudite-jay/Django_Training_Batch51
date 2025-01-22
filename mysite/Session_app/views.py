from django.shortcuts import render
from django.http import JsonResponse
from . models import User
# Create your views here.

def login_view(request):
    if request.session.get('username'):
        return JsonResponse({
            "success": True,
            "user": request.session.get('username'),
            "message": "User is already logged in"
        }, status=400)
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=User.objects.get(username=username)

        if user.password==password:
            request.session.set_expiry(10) 
            request.session['username'] = username
            return JsonResponse({
               " success": True,
               " message": "Login Successful"
            },status=200)
        
    return render(request, 'Session_app/login.html')