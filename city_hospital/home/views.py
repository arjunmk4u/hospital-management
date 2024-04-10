from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Booking(request):
    return render(request, 'booking.html')

def Doctors(request):
    return render(request, 'doctors.html')

def Contact(request):
    return render(request, 'contact.html')

def departmnet(request):
    return render(request, 'department.html')