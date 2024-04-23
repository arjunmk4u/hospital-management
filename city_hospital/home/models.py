from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()

    def __str__(self):
        return self.dept_name

class doctors(models.Model):
    doc_name = models.CharField(max_length=50)
    doc_spec = models.CharField(max_length=100)
    doc_dept = models.ForeignKey(departments, on_delete=models.CASCADE, default=None)
    doc_image = models.ImageField(upload_to='doctors')

    def __str__(self):
        return f"Dr {self.doc_name} - ({self.doc_spec})"

class booking(models.Model):
    p_name = models.ForeignKey(User, on_delete=models.CASCADE)
    p_phone = models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(doctors, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)


    