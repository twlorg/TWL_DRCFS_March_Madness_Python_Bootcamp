
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name="todo"),
    path('del/<str:item_id>', views.remove, name="del"),
    path('register/', views.register_request, name="register"),
    path('login/', views.login_request, name="login")
]
