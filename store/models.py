from django.db import models
from django.contrib.auth.models import User

    
class Student(models.Model):
    reg_no = models.CharField(max_length=40)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=20)

    def __str__(self):
        return self.department_name

class Program(models.Model):
    program_name = models.CharField(max_length=100)
    program_code = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.program_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    description = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    credit = models.PositiveIntegerField()
    course_year = models.PositiveIntegerField()
  

    def __str__(self):
        return self.course_name