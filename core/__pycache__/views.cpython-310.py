o
    ��;f�  �                   @   s�   d dl mZmZ d dl mZ d dlmZmZmZ d dlZd dl	m
Z
 d dlmZmZmZ d dlmZ dd	� Zd
d� Zdd� Zdd� Ze
dd� �Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zd d!� ZdS )"�    )�render�redirect)�get_object_or_404)�
Department�Program�CourseN)�login_required)�login�logout�authenticate)�Userc                 C   �
   t | d�S )Nz
index.html�r   ��request� r   �!E:\python\timetable\core\views.py�home
   �   
r   c                 C   r   )Nz
about.htmlr   r   r   r   r   �about   r   r   c                 C   s   t | � td�S )Nz
core:login)r
   r   r   r   r   r   �logout_view   s   r   c                 C   sd   d}| j dkr(| j�d�}| j�d�}t||d�}|d ur&t| |� td�S d}d|i}t| d	|�S )
N� �POST�username�password)r   r   zcore:dashboardzInvalid Username Or Password�	login_errzcore/login.html)�methodr   �getr   r	   r   r   )r   r   r   r   �user�contextr   r   r   �
login_view   s   

�r    c                 C   r   )Nzcore/dashboard.htmlr   r   r   r   r   �	dashboard'   s   
r!   c                 C   s   t j�� }d|i}t| d|�S )N�departmentszcore/staff.html)r   �objects�allr   )r   r"   r   r   r   r   �staff+   s   
�r%   c                 C   r   )Nzcore/feedback.htmlr   r   r   r   r   �feedback5   r   r&   c                 C   s  t t|d�}tjj|d�}i }|D ]}|j}||vrg ||< || �|� q| jdkr�| j�	d�}| j�	d�}| j�	d�}| j�	d�}	| j�	d�}
| j�	d	�}|rltjj	|d�}||_
||_|	|_||_|
|_|��  ntjj|||
||	|d
�}|��  td|jd�S |||d�}t| d|�S )N��pk��programr   �cId�c_code�c_name�	c_credits�c_desc�course_year)�course_name�course_code�descriptionr*   �creditr0   �core:course)r*   �courses�courses_by_yearzpages/course.html)r   r   r   r#   �filterr0   �appendr   r   r   r2   r1   r4   r3   �save�creater   r(   r   )r   r*   r6   r7   �course�yearr+   r,   r-   r.   r/   r0   r   r   r   r   r<   9   s>   

�r<   c                 C   �&   t jj|d�}|��  td|jjd�S )Nr'   r5   r)   )r   r#   r   �deleter   r*   �id)r   r(   r<   r   r   r   �deleteCoursed   �   rA   c           	      C   s�   t jj|d�}tj�� }| jdkrD| j�d�}| j�d�}| j�d�}|r7tjj|d�}||_||_|�	�  ntjj
|||d�}|�	�  ||d�}t| d|�S )	Nr'   r   ZprgIdZprgcodeZprgname)�program_code�program_name�
department)rE   �programszpages/program.html)r   r#   r   r   r$   r   r   rC   rD   r:   r;   r   )	r   �dptrE   rF   Zprg_idZprogcodeZprognamer*   r   r   r   r   r*   i   s"   


�r*   c                 C   r>   )Nr'   zcore:program)rG   )r   r#   r   r?   r   rE   r@   )r   r(   r*   r   r   r   �deleteProgram�   rB   rH   c                 C   s�   t j�� }| jdkrC| j�d�}| j�d�}| j�d�}|r3t jj|d�}||_||_|��  t
d�S t jj	||d�}|��  t
d�S d|i}t| d	|�S )
Nr   ZdtIdZdptcodeZdptnamer'   )�department_code�department_name�core:departmentsr"   zcore/departments.html)r   r#   r$   r   r   r   rI   rJ   r:   r;   r   r   )r   r"   Zdpt_idZdpt_codeZdpt_namerE   r   r   r   r   r"   �   s    

�r"   c                 C   s   t jj|d�}|��  td�S )Nr'   rK   )r   r#   r   r?   r   )r   r(   rE   r   r   r   �
deleteDept�   s   rL   )Zdjango.shortcutsr   r   r   Zstore.modelsr   r   r   �datetimeZdjango.contrib.auth.decoratorsr   �django.contrib.authr	   r
   r   �django.contrib.auth.modelsr   r   r   r   r    r!   r%   r&   r<   rA   r*   rH   r"   rL   r   r   r   r   �<module>   s*    

+