from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'staff/login.html')

def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')
