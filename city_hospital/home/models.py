from django.db import models

# Create your models here.

class departments(models.Model):
    dept_name = models.CharField(max_length=100)
    dept_desc = models.TextField()