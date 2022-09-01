from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('index/', views.index, name = "Home"),
    path('about/', views.about, name = "About"),
    path('Contact_us/', views.Contact_us, name = "Contact_us"),
]