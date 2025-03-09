from django.contrib import admin
from django.urls import path
from .views import plant_model

urlpatterns = [
    path('predict/', plant_model, name="model"),
]