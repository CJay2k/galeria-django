"""galeria_zdjec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from photos.views import photo_list, add_photo_view, delete_photo, delete_photo_list, profile, home

urlpatterns = [
    path('supers3cret4dm1n/', admin.site.urls),
    path('', photo_list, name='photo_list'),
    url(r'^accounts/', include('allauth.urls')),
    path('add/', add_photo_view, name='add_photo_view'),
    path('delete/', delete_photo_list, name='delete_photo_list'),
    path('delete/<int:pk>/', delete_photo, name='delete_photo'),
    path('u/', home),
    url(r'u/(?P<username>.+)/$', profile, name="profile"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
