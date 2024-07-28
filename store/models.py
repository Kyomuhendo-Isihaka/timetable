from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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

class Staff(models.Model):
    ROLE = [('Admin','Admin'),('Lecturer','Lecturer')]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=50, choices=ROLE, default='lecturer')

    def delete(self, *args, **kwargs):
        courses = Course.objects.filter(course_lecturer=self)
        for course in courses:
            course.course_lecturer = None
            course.save()
        super().delete(*args, **kwargs)
    

    def __str__(self):
        return self.username
    
class Course(models.Model):
    course_lecturer = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=20)
    description = models.TextField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    credit = models.PositiveIntegerField()
    course_year = models.CharField(max_length=40)
  
    def __str__(self):
        return self.course_name
    


    

class Student(models.Model):
    reg_no = models.CharField(max_length=40)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Room(models.Model):
    room_name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class TimeSlot(models.Model):
    DAY_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    TIME_RANGE_CHOICES = (
        ('08:00-11:00', '08:00-11:00'),
        ('11:00-14:00', '11:00-14:00'),
        ('14:00-17:00', '14:00-17:00'),
    )

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    time_range = models.CharField(max_length=11, choices=TIME_RANGE_CHOICES)

    def __str__(self):
        return f"{self.day} - {self.time_range}"
    
class Timetable(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    year = models.CharField(max_length=10)
    
    def __str__(self):
        return f"Timetable for {self.program.program_name} Year {self.year}"
    

class CourseSchedule(models.Model):
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.course_name} in {self.room.room_name} at {self.timeslot}"

    def save(self, *args, **kwargs):
        self.validate_schedule()
        super().save(*args, **kwargs)

    def validate_schedule(self):
        # Check for room conflicts
        room_conflicts = CourseSchedule.objects.filter(
            room=self.room,
            timeslot=self.timeslot
        ).exclude(id=self.id)
        if room_conflicts.exists():
            raise ValidationError(f"Room {self.room.room_name} is already booked for {self.timeslot}.")

        # Check for staff conflicts
        staff_conflicts = CourseSchedule.objects.filter(
            staff=self.staff,
            timeslot=self.timeslot
        ).exclude(id=self.id)
        if staff_conflicts.exists():
            raise ValidationError(f"Staff {self.staff.username} is already scheduled for another course at {self.timeslot}.")
