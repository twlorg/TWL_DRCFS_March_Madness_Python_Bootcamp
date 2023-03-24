from django.contrib import admin
from django.urls import path


from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamroapp/', views.main),
    path('another/', views.another),
    path('form/', views.testing_form),
    path('new/', views.good_form)
]
