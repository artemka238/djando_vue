from django.db import models

class Article(models.Model):
    name = models.CharField(max_length = 100)

class Doctor(models.Model):
    name = models.CharField(max_length = 1400)
    speciality = models.CharField(max_length = 100)
    
    def __str__(self) -> str:
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length = 1500)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor)

    def __str__(self) -> str:
        return self.name
    
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, models.CASCADE)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.patient}-{self.doctor}-{self.date}" 
    
class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, models.CASCADE)
    diagnosis = models.TextField()

    def __str__(self) -> str:
        return f"{self.patient}-{self.diagnosis}" 
