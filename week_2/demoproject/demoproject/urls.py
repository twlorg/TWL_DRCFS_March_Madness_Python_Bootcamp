from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hamroapp/', views.main),
    path('another/', views.another),
    path('form/', views.testing_form),
    path('new/', views.good_form)
]

#urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
