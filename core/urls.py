
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from django.shortcuts import render
from django.conf.urls import handler404
from mercado.views import custom_page_not_found

handler404 = custom_page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mercado.urls'))
]