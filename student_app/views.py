from django.shortcuts import render, redirect
from store.models import Student
from django.contrib import messages
from django.contrib.auth import logout

def login_view(request):
    if request.method == "POST":
        reg_no = request.POST.get('reg_no')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(reg_no=reg_no)
            if student.password == password:
                request.session['student_id'] = student.id
                return redirect('student:dashboard')
            else:
                messages.error(request, 'Invalid password.')
        except Student.DoesNotExist:
            messages.error(request, 'Student with this registration number does not exist.')
    return render(request, 'students/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('student:login')

def student_dashboard(request):
    if 'student_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page.')
        return redirect('student:login')
    return render(request, 'students/student_dashboard.html')

def student_departments(request):
    if 'student_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page.')
        return redirect('student:login')
    return render(request, 'students/student_departments.html')

def student_lecturers(request):
    if 'student_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page.')
        return redirect('student:login')
    return render(request, 'students/student_lecturers.html')

def student_rooms(request):
    if 'student_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page.')
        return redirect('student:login')
    return render(request, 'students/student_rooms.html')

def settings(request):
    if 'student_id' not in request.session:
        messages.error(request, 'You need to be logged in to view this page.')
        return redirect('student:login')
    return render(request, 'students/settings.html')
