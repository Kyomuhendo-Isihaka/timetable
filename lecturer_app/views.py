from django.shortcuts import render

# Create your views here.
def lecturer_dashboard(request):
    return render(request, 'lecturers/lecturer_dashboard.html')
