from django.contrib import admin
from django.urls import path
from .views import plant_model, predict_disease

urlpatterns = [
    path('', plant_model, name="welcome"),
    path('predict/', predict_disease, name="model"),
]