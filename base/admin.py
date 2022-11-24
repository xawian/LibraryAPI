from django.contrib import admin
from .models import Employee, Category, Release, Author, Status, Book, Client, Hire, Return, Assesment
# Register your models here.

admin.site.register(Employee)
admin.site.register(Category)
admin.site.register(Release)
admin.site.register(Author)
admin.site.register(Status)
admin.site.register(Book)
admin.site.register(Client)
admin.site.register(Hire)
admin.site.register(Return)
admin.site.register(Assesment)
