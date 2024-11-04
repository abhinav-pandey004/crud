from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("index",views.index,name='home'),
   path("add_book",views.add_book,name='add_book'),
   path("add_author",views.add_author,name='add_author'),
   path("create_book",views.create_book,name='create_book'),
]