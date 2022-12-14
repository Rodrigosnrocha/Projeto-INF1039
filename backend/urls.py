"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from backend.eventos import views as evento_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lugar/', include('backend.lugar.urls')),                      # Include urls.py do app lugar aonde tem todos os urls para cada API de lugar
    path('api/eventos/', include('backend.eventos.urls')),                 # Lista e criacao de eventos
    path('api/auth/', include('backend.conta.urls')),
]

# Link para a foto de cada lugar
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
