from django.db import models

# Create your models here.
class Appointment(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    date=models.DateTimeField()
<<<<<<< HEAD
    status=models.CharField(max_length=100,default="Pending")
=======
    status=models.CharField(max_length=100,default="success")
>>>>>>> 035c312 (design)

    def __str__(self):
        return self.name
    
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=15)
    speciality=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.name