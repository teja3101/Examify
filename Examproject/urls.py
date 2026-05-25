from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('examapp/', include('Examapp.urls')),
     path('', lambda request: redirect('/examapp/loginuser/')),
]