from django.contrib import admin
from .models import departments, doctors
# Register your models here.

admin.site.register(departments)

class DocAdmin(admin.ModelAdmin):
    list_display = ('doc_name', 'doc_spec', 'doc_dept')
admin.site.register(doctors, DocAdmin)