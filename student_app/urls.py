from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
        path('dashboard/', views.student_dashboard, name='dashboard'),
        path('departments/', views.student_departments, name='departments'),
        path('lecturers/', views.student_lecturers, name='lecturers'),
        path('rooms/', views.student_rooms, name='rooms'),
        path('login/', views.login_view, name = 'login'),
        path('logout/', views.logout_view, name = 'logout'),
        path('settings/', views.settings, name='settings'),
    ]