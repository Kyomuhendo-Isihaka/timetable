from django.contrib import admin
from django.urls import path
from . import views

app_name = 'lecturer'

urlpatterns = [
        path('dashboard/', views.lecturer_dashboard, name='dashboard'),
    ]