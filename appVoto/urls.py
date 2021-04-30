"""appVoto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('ayuda/', views.ayuda, name="ayuda"),
    path('scanner/', views.scanner, name="scanner"),
    path('scannerResult/', views.scannerResult, name="scannerResult"),
    path('procesosElectorales/', views.procesosElectorales, name="procesosElectorales"),
    path('boleta/', views.boleta, name="boleta"),
    path('generadorVoto/', views.generadorVoto, name="generadorVoto"),
    path('votoQr/', views.votoQr, name="votoQr"),
    path('boletaInside/', views.boletaInside, name="boletaInside"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)