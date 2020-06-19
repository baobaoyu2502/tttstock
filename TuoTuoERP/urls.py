"""TuoTuoERP URL Configuration

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
from django.urls import path
from storage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('base/',views.base),
    path('test/', views.test),
    path('stockList/', views.stockList),
    path('stockIn/',views.stockIn),
    path('stockOut/', views.stockOut),
    path('stocklistview/',views.stocklistview),
    path('orderList/', views.orderList),
    path('search/', views.search_item),
]
