from django.contrib import admin
from app.models import Appointment, Doctor

# Register the Appointment model

# Define a custom admin for the Doctor model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'speciality', 'email']

class Aadmin(admin.ModelAdmin):
    list_display = ['id','name', 'date']

# Register the Doctor model with the custom admin class
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment,Aadmin)
