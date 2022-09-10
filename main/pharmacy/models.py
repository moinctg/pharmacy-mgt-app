from argparse import ONE_OR_MORE
from datetime import datetime
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
    def __str__(self):
        return self.name

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
    def __str__(self):
        return self.name
class Medicine(models.Model):
    mfg = models.DateTimeField(auto_now_add='')
    name= models.CharField(max_length=20)
    quntity=models.BigIntegerField()
    price=models.BigIntegerField()
    manafucture= models.CharField(max_length=20)
    exp_date = models.DateTimeField(auto_now_add='')


class Stock(models.Model):
    # product = models.ForeignKey('Medicine',on_delete=models.CASCADE)
    name=models.ForeignKey('Medicine',on_delete=models.CASCADE)
    # manafucture=models.ForeignKey('Medicine',on_delete=models.CASCADE)
    price= models.BigIntegerField()
    quntity=models.BigIntegerField()
    waranty=models.BigIntegerField()
    purchase_date=models.DateTimeField(auto_now_add='')
    sub_total = models.BigIntegerField()

class StoreKipper(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    nid=models.CharField(max_length=50)
    Salary=models.BigIntegerField()
    join_date=models.DateTimeField(auto_now_add='')



class Store(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    location=models.CharField(max_length=50)
    store_kiper= models.ForeignKey('StoreKipper',on_delete=models.CASCADE)

