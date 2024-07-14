# # forms.py

# from django import forms
# from store.models import Program, Course, Room, TimeSlot, Staff, CourseSchedule

# class TimetableForm(forms.Form):
#     program = forms.ModelChoiceField(queryset=Program.objects.all(), label="Program")
#     year = forms.IntegerField(label="Year")

# class CourseScheduleForm(forms.ModelForm):
#     class Meta:
#         model = CourseSchedule
#         fields = ['course', 'room', 'timeslot', 'staff']
    
#     course = forms.ModelChoiceField(queryset=Course.objects.all(), label="Course")
#     room = forms.ModelChoiceField(queryset=Room.objects.all(), label="Room")
#     timeslot = forms.ModelChoiceField(queryset=TimeSlot.objects.all(), label="Timeslot")
#     staff = forms.ModelChoiceField(queryset=Staff.objects.all(), label="Lecturer")

# from django import forms
# from store.models import Program

# class GenerateTimetableForm(forms.Form):
#     program = forms.ModelChoiceField(queryset=Program.objects.all())
#     year = forms.IntegerField()

from django import forms
from store.models import Program

class GenerateTimetableForm(forms.Form):
    program_id = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label="Select a Program", label="Program")
    year = forms.IntegerField(label="Year")
