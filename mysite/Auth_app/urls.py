from django.urls import path
from . import views

urlpatterns = [
   path("print-hello/",views.hello_world),
   path("home/",views.home_page),
   path("all-data/",views.all_data),
]
