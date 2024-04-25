from django.shortcuts import render, redirect
from .models import departments, doctors, booking
from .forms import BookingForm, createUser, userLogin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import Group
from .decorators import groups_required
from django.urls import reverse
# Create your views here.


def logout_required(view_func):
    @login_required
    def _wrapped_view(request):
        return redirect('home')
    return _wrapped_view



def index(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return render(request,'index.html')

def about(request):
    return render(request, 'about.html')

def Booking(request):

    if request.method == 'GET':
        # doc_name = request.GET.get('doctor_name')
        doc_name =  request.session.get('doctor_name')
        print(doc_name)
        form = BookingForm(
            initial={
                'doc_name':doc_name,
                'p_name': request.user,
                'p_email':request.user.email
            })
        return render(request, 'booking.html', {'form': form})

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Appointment Booked")
            form = BookingForm()


    dict_form = {
        'form' : form
        
    }
    return render(request, 'booking.html', dict_form)

@login_required(login_url= '/login')
def Doctors(request):
    dict_doc = {
        "doc" : doctors.objects.all(),
        "dep" : 'department'
    }

    if request.method == 'GET':
        doc_dep = request.session.get('dept_value')
        doc_dep_name = request.session.get('dept_name')
        filtered_doc_dept = doctors.objects.filter(doc_dept = doc_dep)
        print(filtered_doc_dept)
        dict_doc['doc'] = filtered_doc_dept
        dict_doc['dep'] = doc_dep_name
        if doc_dep_name == None:
            dict_doc['doc'] = doctors.objects.all()

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
    if request.method == 'POST':
        dept_value = request.POST.get("dept_value")
        dept_name = request.POST.get("dept_name")
        print(dept_value)
        request.session['dept_value'] = dept_value
        request.session['dept_name'] = dept_name
        return redirect('doctors')
    return render(request, 'department.html', dict_dept)


def register(request):
    form = createUser()
    if request.method =='POST':
        form = createUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name = 'users')
            user.groups.add(group)
            messages.success(request, f"Account crated for {username}")
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
                if request.user.is_authenticated:
                    if request.user.groups.filter(name='admin').exists():
                        return redirect('admin:index')
                    elif request.user.groups.filter(name='users').exists():
                        return redirect('profile')
                    elif request.user.groups.filter(name='Doctor').exists():
                        return redirect('docpanel')
            else:
                messages.info(request, 'Username or password is incorrect')

    return render(request, 'login.html', {'form': form})    


@login_required(login_url= '/login')
@groups_required(['users', 'admin'])
def profile(request):
    return render(request, "profile.html")

@login_required(login_url='login')
def viewBooking(request):
    data = booking.objects.all().filter(p_name = request.user)
    for field in data:
        print(field)
    return render(request, 'userbookings.html', {'data' : data})

def deleteBooking(request, did):
    booking.objects.get(id= did).delete()
    return redirect('userbookings')

def editBooking(request, eid):
    edit_data = booking.objects.get(id= eid)
    return render(request, 'userbookings.html', {'edit_data': edit_data})


def logoutUser(request):
    logout(request)
    return redirect('home')

def docpanel(request):
    doc = doctors.objects.get(doc_name = request.user)
    data = booking.objects.all().filter(doc_name = doc)
    print(data)
    return render(request, 'doctor_panel.html', {'data' : data})