from django.shortcuts import render, redirect
from .models import departments, doctors
from .forms import BookingForm, createUser
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Booking(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    form = BookingForm
    dict_form = {
        'form' : form
    }
    return render(request, 'booking.html', dict_form)

def Doctors(request):
    dict_doc = {
        "doc" : doctors.objects.all()
    }

    if request.method == "POST":
        doc = request.POST.get("name")
        print(doc)
        return redirect('booking')


    return render(request, 'doctors.html', dict_doc)

def Contact(request):
    return render(request, 'contact.html')

def departmnet(request):
    dict_dept = {
        "dept" : departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)


def register(request):
    form = createUser()
    context = { 'form' : form}
    return render(request, 'register.html', context)


def login(request):
    return render(request, 'login.html')