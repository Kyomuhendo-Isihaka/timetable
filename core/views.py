from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from store.models import Department, Program, Course,Staff
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render (request, 'about.html')

def logout_view(request):
    logout(request)
    return redirect('core:login')

def login_view(request):
    login_err=""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:dashboard')
        else:
            login_err="Invalid Username Or Password"

    context = {
            'login_err':login_err,
        }
                   
    return render(request, 'core/login.html',context)

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

def staff(request):
    departments = Department.objects.all()
    staffs = Staff.objects.all()
   
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        dpt = request.POST.get('department')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_pass = request.POST.get('conf_password')

        department = Department.objects.get(pk=dpt)
    

        if staff_id:
            print('editing')
        else:
            if password==conf_pass:
                staff = Staff.objects.create(department=department, username=username, email=email,password=password)
                staff.save()
            else:
                messages.error(request, "Passwords do not match")
                

    context = {
        'departments':departments,
        'staffs':staffs,
    }
    return render(request, 'core/staff.html', context)



def feedback(request):
    return render(request, 'core/feedback.html')


def course(request, program):
    program = get_object_or_404(Program, pk=program)
    courses = Course.objects.filter(program=program)

    courses_by_year = {}
    for course in courses:
        year = course.course_year  
        if year not in courses_by_year:
            courses_by_year[year] = []
        courses_by_year[year].append(course)

    if request.method == "POST":
        cId = request.POST.get('cId')
        c_code = request.POST.get('c_code')
        c_name = request.POST.get('c_name')
        c_credits = request.POST.get('c_credits')
        c_desc = request.POST.get('c_desc')
        course_year = request.POST.get('course_year')

        if cId:
            course = Course.objects.get(pk=cId)
        
            course.course_code = c_code
            course.course_name = c_name
            course.credit = c_credits
            course.course_year = course_year
            course.description = c_desc
        
            course.save()

        else:
            course = Course.objects.create(course_name= c_name, course_code = c_code, description= c_desc,  program=program, credit=c_credits, course_year=course_year)
            course.save()
        return redirect('core:course', program=program.pk)


    context = {
        'program':program,
        'courses':courses,
        'courses_by_year':courses_by_year,
    }
    return render(request, "pages/course.html", context)

def deleteCourse(request, pk):
    course= Course.objects.get(pk=pk)
    course.delete()
    return redirect('core:course', program=course.program.id)

def program(request, dpt):
    department = Department.objects.get(pk = dpt)
    programs = Program.objects.all()

    if  request.method=="POST":
        prg_id = request.POST.get('prgId')
        progcode = request.POST.get('prgcode')
        progname = request.POST.get('prgname')

        if prg_id: 
           
            program = Program.objects.get(pk=prg_id)
            program.program_code = progcode
            program.program_name = progname
            program.save()

        else:
            program = Program.objects.create(program_code = progcode, program_name=progname, department=department)
            program.save()

    context={
        'department':department,
        'programs':programs,
    }   

    return render(request, 'pages/program.html', context)

def deleteProgram(request, pk):
    program = Program.objects.get(pk=pk)
    program.delete()
    return redirect('core:program', dpt=program.department.id)
   

def departments(request):
    departments = Department.objects.all()
    if request.method == "POST":
        dpt_id = request.POST.get('dtId')
        dpt_code = request.POST.get('dptcode')
        dpt_name = request.POST.get('dptname')

        if dpt_id: 
            department = Department.objects.get(pk=dpt_id)
            department.department_code = dpt_code
            department.department_name = dpt_name
            department.save()

        else:
            department = Department.objects.create(department_code = dpt_code, department_name = dpt_name)
            department.save()

        return redirect('core:departments')

    context = {'departments': departments}
      
    return render(request, 'core/departments.html', context)

def students(request):
    return render(request, 'core/student.html')

def deleteDept(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('core:departments')