from django.contrib import admin
from .models import Department, Program, Course,Staff,Student,Room,TimeSlot, Timetable, CourseSchedule

# Register your models here.
admin.site.register(Department)
admin.site.register(Program)
admin.site.register(Course)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Room)
admin.site.register(TimeSlot)
admin.site.register(Timetable)
admin.site.register(CourseSchedule)

