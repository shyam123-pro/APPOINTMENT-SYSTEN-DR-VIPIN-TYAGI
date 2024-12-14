from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse  # Use JsonResponse for standard Django views
import json  # To parse the request body
from app.models import Appointment  # Import the Appointment model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Doctor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from app.serializers import AppointmentSerializer,DoctorSerializer
from .models import Doctor

# Create your views here.
def home(req):
    return render(req, 'index.html')

@csrf_exempt
def doctor_login(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            # Validate credentials
            doctor = Doctor.objects.filter(email=email, password=password).first()

            if doctor:
                # Success response
                return JsonResponse({
                    "success": True,
                    "message": "Login successful",
                    "doctor": {
                        "id": doctor.id,
                        "name": doctor.name,
                        "mobile": doctor.mobile,
                        "speciality": doctor.speciality,
                        "email": doctor.email
                    }
                }, status=200)
            else:
                # Invalid credentials response
                return JsonResponse({
                    "success": False,
                    "message": "Invalid email or password"
                }, status=401)
        except Exception as e:
            # Error handling
            return JsonResponse({
                "success": False,
                "message": f"An error occurred: {str(e)}"
            }, status=500)
    else:
        # Method not allowed response
        return JsonResponse({
            "success": False,
            "message": "Only POST method is allowed"
        }, status=405)

@csrf_exempt
def book_appointment(req):
    if req.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(req.body)
            print(data)  # Log the data for debugging
            
            # Extract required fields
            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')
            mobile = data.get('mobile')
            appointment_date = data.get('appointmentDate')
            
            # Validate required fields
            if not all([name, age, gender, mobile, appointment_date]):
                return JsonResponse({'error': 'All fields are required.'}, status=400)
            
            # Save to the database
            appointment = Appointment(
                name=name,
                age=age,
                gender=gender,
                mobile=mobile,
                date=appointment_date
            )
            appointment.save()
            
            # Return success response
            return JsonResponse({'success': 'Appointment booked successfully.'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            print(f"Error: {e}")  # Log unexpected errors
            return JsonResponse({'error': 'An error occurred while booking the appointment.'}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)


def get_appointments(req):
    if(req.method=="GET"):
        appointments=Appointment.objects.all()
        s_a=AppointmentSerializer(appointments,many=True)
        print(appointments)
        return JsonResponse({"success":s_a.data},status=200)
    else:
        return JsonResponse({"error":"Get Method required"},status=400)
    

def get_doctor(request, id):
    if request.method == "GET":
        try:
            doctor = Doctor.objects.get(id=id)
            serialized_doctor = DoctorSerializer(doctor)
            return JsonResponse(serialized_doctor.data, safe=False)
        except Doctor.DoesNotExist:
            return JsonResponse({"error": "Doctor not found"}, status=404)
    else:
        return JsonResponse({"error": "Only GET method is allowed"}, status=405)
<<<<<<< HEAD
=======





from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Appointment

@csrf_exempt
def update_appointment(req,id):
    if req.method == 'POST':
        try:
            # Parse JSON data from the request body
            data = json.loads(req.body)
            
            # Extract the appointment ID and other required fields
            appointment_id = id

            name = data.get('name')
            age = data.get('age')
            gender = data.get('gender')
            mobile = data.get('mobile')
            appointment_date = data.get('appointmentDate')
            
            # Check if appointment ID is provided
            if not appointment_id:
                return JsonResponse({'error': 'Appointment ID is required.'}, status=400)
            
            # Validate the fields
            if not all([name, age, gender, mobile, appointment_date]):
                return JsonResponse({'error': 'All fields are required.'}, status=400)
            
            # Try to fetch the appointment by its ID
            try:
                appointment = Appointment.objects.get(id=appointment_id)
            except Appointment.DoesNotExist:
                return JsonResponse({'error': 'Appointment not found.'}, status=404)

            # Update the fields of the appointment
            appointment.name = name
            appointment.age = age
            appointment.gender = gender
            appointment.mobile = mobile
            appointment.date = appointment_date
            appointment.save()
            
            # Return success response
            return JsonResponse({'success': 'Appointment updated successfully.'}, status=200)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
        except Exception as e:
            print(f"Error: {e}")  # Log any other unexpected errors
            return JsonResponse({'error': 'An error occurred while updating the appointment.'}, status=500)
    
    else:
        # Method Not Allowed response
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)






from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Appointment

@csrf_exempt
def cancel_appointment(request, appointment_id):
    if request.method == 'DELETE':
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.delete()
            return JsonResponse({'message': 'Appointment canceled successfully!'}, status=200)
        except Appointment.DoesNotExist:
            return JsonResponse({'error': 'Appointment not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)
>>>>>>> 035c312 (design)
