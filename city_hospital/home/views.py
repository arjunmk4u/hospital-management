from django.shortcuts import render
from .models import departments, doctors
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Booking(request):
    return render(request, 'booking.html')

def Doctors(request):
    dict_doc = {
        "doc" : doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doc)

def Contact(request):
    return render(request, 'contact.html')

def departmnet(request):
    dict_dept = {
        "dept" : departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)