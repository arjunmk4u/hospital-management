from django import forms
from .models import booking, register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'

        

        widgets = {
            'booking_date' : DateInput()
        }
        labels = {
            'p_name' : "Patient Name",
            'p_phone' : "Phone Number",
            'p_email' : "E-Mail",
            'doc_name' : "Doctor",
            'booking_date' : "Booking Date"
        }

class createUser(forms.ModelForm):
    class Meta:
        model = register
        fields = '__all__'