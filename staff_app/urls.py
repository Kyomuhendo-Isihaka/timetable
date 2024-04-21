from django.contrib import admin
from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
        path('dashboard/', views.staff_dashboard, name='dashboard'),
        path('login/', views.login_view, name = 'login'),
    ]