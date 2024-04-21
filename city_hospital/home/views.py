from django.shortcuts import render, redirect
from .models import departments, doctors
from .forms import BookingForm, createUser, userLogin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def Booking(request):

    if request.method == 'GET':
        # doc_name = request.GET.get('doctor_name')
        doc_name = f" Dr {request.session.get('doctor_name')}"
        print(doc_name)
        form = BookingForm(initial={'doc_name':doc_name})
        return render(request, 'booking.html', {'form': form})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()

    dict_form = {
        'form' : form
        
    }
    return render(request, 'booking.html', dict_form)

def Doctors(request):
    dict_doc = {
        "doc" : doctors.objects.all()
    }

    if request.method == "POST":
        doc = request.POST.get("doctor_name")
        request.session['doctor_name'] = doc
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
    if request.method =='POST':
        form = createUser(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f"Account crated for {user}")
        else:
            error = form.errors.as_ul()
            print(error)
            messages.error(request, error)
    context = { 'form' : form}
    return render(request, 'register.html', context)


def login_view(request):
    form = userLogin()
    if request.method =='POST':
        form = userLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username= username, password= password)
            if user is not None:
                login(request,user)
                return redirect('profile')

    return render(request, 'login.html', {'form': form})    


def profile(request):
    return render(request, "profile.html")

def logoutUser(request):
    logout(request)
    return redirect('login')