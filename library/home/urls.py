from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("index",views.index,name='home'),
   path("add_book/<int:author_id>/",views.add_book,name='add_book'),
   path("add_author",views.add_author,name='add_author'),
   path('update/<str:id>',views.update,name="update"),
   path('delete_book/<str:id>',views.delete_book,name="delete_book"),
]       