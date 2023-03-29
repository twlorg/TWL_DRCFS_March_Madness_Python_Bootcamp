
from django.contrib import admin
from django.urls import path
from . import views
 
urlpatterns = [
    #####################home_page###########################################
    path('', views.index, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    # pass item_id as primary key to remove that the todo with given id
    path('del/<str:item_id>', views.remove, name="del"),
    ########################################################################
]