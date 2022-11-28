from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('add/', views.addBook),
    path('clients/', views.getClients),
    path('register/', views.createUser),
    path('hire/', views.createHire),
    path('hires/', views.getAllHires),
    path('books/<str:book_name>', views.getBookByString),
    path('clients/<str:login>', views.getClientByLogin),
    path('deletebook/<str:id>', views.deleteBookById),
    path('hiresbyid/<str:id>', views.getHireById),
    path('getclientbyid/<str:id>', views.getClientById),
    path('updatebook/<str:id>', views.updateBook),
]
