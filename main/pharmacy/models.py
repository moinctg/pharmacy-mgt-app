from pyexpat import model
# from statistics import mode
from django.db import models

# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=20)
    address=models.CharField(max_length=60)
    location=models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Doctor (models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=60)
    contact = models.BigIntegerField()
    hospital_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)
class Patient(models.Model):
    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )
    name = models.CharField(max_length=20)
    address=models.CharField(max_length=60)
    gender=models.CharField(max_length=20,choices=gender_category)
    contact = models.BigIntegerField()
    details= models.CharField(max_length=150)
    doctor_id=models.ForeignKey('Doctor',on_delete=models.CASCADE)


# class Medicine(models.Model):
    