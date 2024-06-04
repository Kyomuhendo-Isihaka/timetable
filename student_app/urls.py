from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
        path('dashboard/', views.student_dashboard, name='dashboard'),
        path('login/', views.login_view, name = 'login'),
        path('logout/', views.logout_view, name = 'logout'),
    ]