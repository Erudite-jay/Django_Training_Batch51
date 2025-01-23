from django.contrib.auth.signals import user_logged_in # signal

from django.contrib.auth.models import User #sender
from django.db.models.signals import pre_save # signal
from django.dispatch import receiver


def login_success(sender,request,user,**kwargs): #rec. function
    print(f'User {user.username} logged in')
    print(f'emai: {user.email}')
    print(f'IP Address: {request.get_host()}')
    print(f'sender: {sender}')
    print(f'kwargs: {kwargs}')
    # here we can write the logic to send email to the user 

user_logged_in.connect(login_success, sender=User)

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance,**kwargs): 
    print("---------HEllo i am pre save")
    print(f'sender: {sender}')
    print(f'User pre save: {instance}')
    print(f'kwargs: {kwargs}')
    # here we can write the logic to