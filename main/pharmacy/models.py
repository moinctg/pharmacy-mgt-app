from argparse import ONE_OR_MORE
from datetime import datetime
from django.utils import timezone
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
        
# class Medicine(models.Model):
#     name= models.CharField(max_length=20)
#     image = models.ImageField(upload_to='category/', blank=True, null=True)
#     quntity=models.BigIntegerField()
#     price=models.BigIntegerField()
#     sub_total= models.BigIntegerField()
#     manafucture= models.CharField(max_length=20)
#     mfg = models.DateTimeField(auto_now_add='')
#     exp_date = models.DateTimeField(auto_now_add='')
#     def __str__(self):
#         return self.name
#     def calculation(self,quntity,price):
#         calculation = self.price * self.quntity
#         return calculation


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    
    def __str__(self):
        return str(self.name)



class ExpiredManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().annotate(
            expired=ExpressionWrapper(Q(valid_to__lt=Now()), output_field=BooleanField())
        )

class Stock(models.Model):
    category = models.ForeignKey(Category,null=True,on_delete=models.CASCADE,blank=True)
    drug_imprint=models.CharField(max_length=6 ,blank=True, null=True)
    drug_name = models.CharField(max_length=50, blank=True, null=True)
    drug_color = models.CharField(max_length=50, blank=True, null=True)
    drug_shape = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    manufacture= models.CharField(max_length=50, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    drug_strength= models.CharField(max_length=10, blank=True, null=True)
    valid_from = models.DateTimeField(blank=True, null=True,default=timezone.now)
    valid_to = models.DateTimeField(blank=False, null=True)
    drug_description=models.TextField(blank=True,max_length=1000,null=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    objects = ExpiredManager()
   
    def __str__(self):
        return str(self.drug_name)
   
class StoreKipper(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    nid=models.CharField(max_length=50)
    Salary=models.BigIntegerField()
    join_date=models.DateTimeField(auto_now_add='')
    
class Dispense(models.Model):
    
    patient_id = models.ForeignKey(Patient, on_delete=models.DO_NOTHING,null=True)
    drug_id = models.ForeignKey(Stock, on_delete=models.SET_NULL,null=True,blank=False)
    dispense_quantity = models.PositiveIntegerField(default='1', blank=False, null=True)
    taken=models.CharField(max_length=300,null=True, blank=True)
    stock_ref_no=models.CharField(max_length=300,null=True, blank=True)
    instructions=models.TextField(max_length=300,null=True, blank=False)
    dispense_at = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    storekipper = models.ForeignKey(StoreKipper, on_delete=models.DO_NOTHING,null=True)





class Store(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    contact=models.BigIntegerField()
    location=models.CharField(max_length=50)
    store_kiper= models.ForeignKey('StoreKipper',on_delete=models.CASCADE)

