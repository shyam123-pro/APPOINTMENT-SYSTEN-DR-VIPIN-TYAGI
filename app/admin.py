from django.contrib import admin
from app.models import Appointment, Doctor

<<<<<<< HEAD
# Register the Appointment model (no custom admin needed)
admin.site.register(Appointment)
=======
# Register the Appointment model
>>>>>>> 035c312 (design)

# Define a custom admin for the Doctor model
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'speciality', 'email']

<<<<<<< HEAD

# Register the Doctor model with the custom admin class
admin.site.register(Doctor, DoctorAdmin)
=======
class Aadmin(admin.ModelAdmin):
    list_display = ['id','name', 'date']

# Register the Doctor model with the custom admin class
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Appointment,Aadmin)
>>>>>>> 035c312 (design)
