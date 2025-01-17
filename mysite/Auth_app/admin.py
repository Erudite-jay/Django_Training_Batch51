from django.contrib import admin
from .models import Contact
# Register your models here.

# admin.site.register(Contact)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','full_name', 'email', 'mobile_number', 'country')
    search_fields = ('full_name', 'email', 'mobile_number', 'country')
    list_filter = ('country',"full_name", "email", 'mobile_number')

