from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
   path("",views.index,name='home'),
   path("index",views.index,name='home'),
   path("page_login",views.page_login,name='page_login'),
   path("login_view",views.login_view,name='login_view'),
   path("signup",views.signup,name='signup'),
   path("sign_up",views.sign_up,name='sign_up'),
   path("add_book/",views.add_book,name='add_book'),
   path("add_author",views.add_author,name='add_author'),
   path('update/<str:id>',views.update,name="update"),
   path('delete_book/<str:id>',views.delete_book,name="delete_book"),
]