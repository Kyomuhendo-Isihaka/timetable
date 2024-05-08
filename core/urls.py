from django.contrib import admin
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('feedback/', views.feedback, name='feedback'),
   
    path('staff/', views.staff, name='staff'),

    path('departments/', views.departments, name='departments'),
    path('departments/delete/<int:pk>', views.deleteDept, name='deleteDepartment'),

    path('departments/<str:dpt>/', views.program, name='program'),
    path('program/delete/<int:pk>/', views.deleteProgram, name='deleteProgram'),
    
    path('courses/<str:program>/', views.course, name='course'),
    path('course/delete/<int:pk>/', views.deleteCourse, name='deleteCourse'),


    
]