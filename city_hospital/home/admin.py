from django.contrib import admin
from .models import departments, doctors, booking
# Register your models here.

admin.site.register(departments)

class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_spec', 'doc_dept')
admin.site.register(doctors, DocAdmin)



class BookingAdmin(admin.ModelAdmin):
    list_display = ('p_name', 'p_phone', 'p_email', 'doc_name', 'booking_date', 'booked_on' )
admin.site.register(booking, BookingAdmin)

