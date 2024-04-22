from django import forms
from .models import booking
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class docInput(forms.TextInput):
    input_type = 'text'

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        

        widgets = {
            'booking_date' : DateInput(),
            'doc_name' : docInput(),
            'doc_name': forms.Select(attrs={'readonly': 'readonly'})
        }
        labels = {
            'p_name' : "Patient Name",
            'p_phone' : "Phone Number",
            'p_email' : "E-Mail",
            'doc_name' : "Doctor",
            'booking_date' : "Booking Date"
        }



class createUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']


class userLogin(forms.Form):
    username = forms.CharField(max_length=120, label="username")
    password = forms.CharField(max_length=255, label="password", widget=forms.PasswordInput())
