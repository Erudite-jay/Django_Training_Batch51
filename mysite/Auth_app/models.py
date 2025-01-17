from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    mobile_number=models.CharField(max_length=10)
    country=models.CharField(max_length=100)
