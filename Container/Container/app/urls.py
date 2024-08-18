from django.urls import path
from django.contrib import admin
from app.views import fn

urlpatterns = [

    path('',fn),

]