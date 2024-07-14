from django.contrib import admin
from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
        path('dashboard/', views.staff_dashboard, name='dashboard'),
        path('login/', views.login_view, name = 'login'),
        path('logout/', views.logout_view, name = 'logout'),
        path('settings/', views.settings, name = 'settings'),

        path('generate_timetable/', views.generate_timetable_view, name='generate_timetable'),
    path('success/', views.success_view, name='success_view'),
    path('timetable/', views.timetable_view, name='timetable_view'),
    ]