from django.urls import path, include
from django.contrib import admin
from .views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    #path('accounts/', include('accounts.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    
]

urlpatterns += staticfiles_urlpatterns() #make sure gunicorn find static!!