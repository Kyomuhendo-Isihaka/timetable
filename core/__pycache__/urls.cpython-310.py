o
    ��;f�  �                   @   s�   d dl mZ d dlmZ ddlmZ dZedejdd�ed	ejd
d�edej	dd�edej
dd�edejdd�edejdd�edejdd�edejdd�edejdd�edejdd�edejdd�edejdd�edejdd�gZdS ) �    )�admin)�path�   )�views�core� �home)�namezabout/�aboutzlogin/�loginzlogout/�logoutz
dashboard/�	dashboardzstaff/�staffzdepartments/�departmentszdepartments/delete/<int:pk>ZdeleteDepartmentzdepartments/<str:dpt>/�programzprogram/delete/<int:pk>/�deleteProgramzcourses/<str:program>/�coursezcourse/delete/<int:pk>/�deleteCourseN)�django.contribr   �django.urlsr   r   r   �app_namer   r
   Z
login_viewZlogout_viewr   r   r   Z
deleteDeptr   r   r   r   �urlpatterns� r   r   � E:\python\timetable\core\urls.py�<module>   s$    �