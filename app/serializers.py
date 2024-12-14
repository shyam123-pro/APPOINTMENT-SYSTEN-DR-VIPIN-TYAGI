from app.models import Appointment,Doctor
from rest_framework.serializers import ModelSerializer

class AppointmentSerializer(ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class DoctorSerializer(ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
