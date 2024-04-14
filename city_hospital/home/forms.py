from django import forms

from .models import booking

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