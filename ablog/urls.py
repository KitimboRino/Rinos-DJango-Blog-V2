from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rinosblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
