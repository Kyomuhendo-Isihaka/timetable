from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'core/login.html')

def student_dashboard(request):
    return render(request, 'students/student_dashboard.html')
