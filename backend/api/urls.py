from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router0 = DefaultRouter()
router0.register(r"doctor",views.DoctorAPI)

router1 = DefaultRouter()
router1.register(r"patient",views.PatientAPI)

router2 = DefaultRouter()
router2.register(r"appointment",views.AppointmentAPI)

router3 = DefaultRouter()
router3.register(r"medical_record",views.MedicalRecordAPI)
# ff

urlpatterns = [
    path("",include(router0.urls)),
    path("",include(router1.urls)),
    path("",include(router2.urls)),
    path("",include(router3.urls))
]
