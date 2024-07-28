from django.shortcuts import render, redirect, get_object_or_404
from store.models import Staff, Timetable, CourseSchedule, Program
from django.contrib import messages
from django.contrib.auth import logout
from django.core.management import call_command
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            staff = Staff.objects.get(username=username)
            if staff.password == password:
                request.session['staff_id'] = staff.id
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
    staff_id = request.session.get('staff_id')
    if not staff_id:
        messages.error(request, 'Please log in to access the dashboard.')
        return redirect('staff:login')
    
    staff = get_object_or_404(Staff, id=staff_id)
    context = {
        'staff': staff,
    }
    return render(request, 'staff/staff_dashboard.html', context)

def timetable_view(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        messages.error(request, 'Please log in to access the timetables.')
        return redirect('staff:login')
    
    staff = get_object_or_404(Staff, id=staff_id)
    timetables = Timetable.objects.all().prefetch_related(
        'courseschedule_set__timeslot',
        'courseschedule_set__course',
        'courseschedule_set__staff',
        'courseschedule_set__room'
    )
    course_schedules = CourseSchedule.objects.select_related(
        'course', 'staff', 'room', 'timeslot'
    ).all()

    context = {
        'staff': staff,
        'timetables': timetables,
        'course_schedules': course_schedules,
    }
    return render(request, 'staff/timetable.html', context)

def generate_timetable_view(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        messages.error(request, 'Please log in to generate timetables.')
        return redirect('staff:login')

    staff = get_object_or_404(Staff, id=staff_id)
    
    if request.method == 'POST':
        program_id = request.POST.get('program_id')
        year = request.POST.get('year')

        if program_id and year:
            try:
                # Check if a timetable already exists for the given program and year
                existing_timetable = Timetable.objects.filter(program_id=program_id, year=year).first()
                if existing_timetable:
                    return render(request, 'error_template.html', {'message': 'Timetable already exists for this program and year.'})

                # Convert year to a suitable format if necessary
                year = year.strip()
                program_id = int(program_id)
                call_command('generate_timetable', program_id, year)
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
        context = {
            'staff': staff,
            'programs': programs
        }
        return render(request, 'staff/generate_timetable.html', context)

def success_view(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        messages.error(request, 'Please log in to access the success page.')
        return redirect('staff:login')

    staff = get_object_or_404(Staff, id=staff_id)
    context = {
        'staff': staff
    }
    return render(request, 'staff/success.html', context)

def settings(request):
    staff_id = request.session.get('staff_id')
    if not staff_id:
        messages.error(request, 'Please log in to access the settings.')
        return redirect('staff:login')

    staff = get_object_or_404(Staff, id=staff_id)
    context = {
        'staff': staff
    }
    return render(request, 'staff/settings.html', context)
