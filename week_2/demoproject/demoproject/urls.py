from django.contrib import admin
from django.urls import path,  include

# have to import yo things 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.conf import settings
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamroapp/', views.main),
    path('another/', views.another),
    path('form/', views.testing_form),
    path('new/', views.good_form),
    path('fileupload/', views.fileupload),
    path('context/', views.contextplaying),


    # new way of adding urls (i know it's so cool right? )
    path("", include('todoapp.urls'))
]





urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
