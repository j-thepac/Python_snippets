from django.contrib import admin
from django.urls import path
from . import views
import re
urlpatterns = [
    path('', views.getCT),
]