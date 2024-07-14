from django.shortcuts import render, redirect
from store.models import Staff
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from django.core.management import call_command
# from .forms import GenerateTimetableForm
from store.models import Timetable, CourseSchedule, Program

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            staff = Staff.objects.get(username=username)
            if staff.password == password:
               
                request.session['staff_id'] = staff.id
                staff_id = staff.id 
                
                return redirect('staff:dashboard')  
            else:
                messages.error(request, 'Invalid password.')
        except Staff.DoesNotExist:
            messages.error(request, 'Staff with this username does not exist.')
    return render(request, 'staff/login.html')

def logout_view(request):
    logout(request)
    return redirect('staff:login')

def staff_dashboard(request):
    staff_id = request.session['staff_id']
    staff = get_object_or_404(Staff, id=staff_id)
    
    context = {
        'staff':staff,
    }
    return render(request, 'staff/staff_dashboard.html', context)

def timetable_view(request):
    timetables = Timetable.objects.all().prefetch_related('courseschedule_set__timeslot', 'courseschedule_set__course', 'courseschedule_set__staff', 'courseschedule_set__room')
    course_schedules = CourseSchedule.objects.select_related('course', 'staff', 'room', 'timeslot').all()

    context = {
        'timetables': timetables,
        'course_schedules': course_schedules,
    }
    return render(request, 'staff/timetable.html', context)

# def generate_timetable_view(request):
#     if request.method == 'POST':
#         form = GenerateTimetableForm(request.POST)
#         if form.is_valid():
#             program_id = form.cleaned_data['program']
#             # program_id = 1
#             year = form.cleaned_data['year']
#             call_command('generate_timetable', str(program_id), str(year))
#             return redirect('staff:success_view')
#     else:
#         form = GenerateTimetableForm()
#     return render(request, 'staff/generate_timetable.html', {'form': form})

def generate_timetable_view(request):
    if request.method == 'POST':
        program_id = request.POST.get('program_id')
        year = request.POST.get('year')

        if program_id and year:
            try:
                # Ensure program_id is an integer
                program_id = int(program_id)
                call_command('generate_timetable', program_id, int(year))
                return render(request, 'staff/success.html', {'message': 'Timetable generated successfully'})
            except ValueError:
                return render(request, 'error_template.html', {'message': 'Invalid input. Please select a valid program and year.'})
            except Exception as e:
                return render(request, 'error_template.html', {'message': f'Error generating timetable: {str(e)}'})
        else:
            return render(request, 'error_template.html', {'message': 'Both program and year are required.'})
    else:
        # Fetch programs to populate the dropdown
        programs = Program.objects.all().order_by('program_name')
        return render(request, 'staff/generate_timetable.html', {'programs': programs})

def success_view(request):
    return render(request, 'staff/success.html')


def settings(request):
    return render(request, 'staff/settings.html')