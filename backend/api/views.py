from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import AllowAny


class DoctorAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class PatientAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class AppointmentAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()

class MedicalRecordAPI(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = MedicalRecordSerializer
    queryset = MedicalRecord.objects.all()
