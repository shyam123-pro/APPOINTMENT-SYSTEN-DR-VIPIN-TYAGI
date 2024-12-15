
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home),
    path('api/doctor/login',views.doctor_login),
    path("api/appointment/book", views.book_appointment),
    path("api/appointments", views.get_appointments),
    path("api/doctor/<int:id>", views.get_doctor),


    path("api/appointment/update/<int:id>", views.update_appointment, name="update_appointment"),
   path('api/appointment/cancel/<int:appointment_id>', views.cancel_appointment, name='cancel_appointment'), 
]
