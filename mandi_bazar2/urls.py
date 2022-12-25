from django.contrib import admin
from django.urls import path , include
from django.conf import settings  
from django.conf.urls.static import static  
from . import views
# admin.site.site_header = 'Mandi-Bazar Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('mandi/', include('mainapp.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)