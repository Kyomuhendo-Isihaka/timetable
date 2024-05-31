from django.shortcuts import render, redirect
from store.models import Staff
from django.contrib import messages
from django.contrib.auth import logout
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
    return render(request, 'staff/staff_dashboard.html')
