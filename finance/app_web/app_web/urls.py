"""
URL configuration for app_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from finaces import views

urlpatterns = [
    #path('', views.crear_cliente, name='crear_cliente'),  # Redirigir la URL raíz a la vista de crear cliente
    path('crear-cliente/', views.crear_cliente, name='crear_cliente'),
    path('visualizar-clientes/', views.visualizar_clientes, name='visualizar_clientes'),
    path('', views.visualizar_clientes, name='crear_cliente'),  # Redirigir la URL raíz a la vista de crear cliente
    path('visualizar-transacciones/', views.visualizar_transacciones, name='visualizar_transacciones'),
]
