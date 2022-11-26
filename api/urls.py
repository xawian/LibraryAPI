from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addBook),
    path('clients/', views.getClients),
    path('register/', views.createUser)
]
