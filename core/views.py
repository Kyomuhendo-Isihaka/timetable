from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from store.models import Department, Program, Course
import datetime

# Create your views here.
def login_view(request):
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')







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
      
    return render(request, 'departments.html', context)

def deleteDept(request, pk):
    department = Department.objects.get(pk=pk)
    department.delete()
    return redirect('core:departments')