"""UploadImages URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from UploadImages import settings
from django.conf.urls.static import static

urlpatterns = [
	path('', imagesList),
    path('admin/', admin.site.urls),
    path('images_list/', imagesList),
    re_path(r'add_image/.{0,9999}', addImage, name='add_image'),
    re_path(r'edit_image/.{0,9999}', editImage, name='edit_image'),

   
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)