from argparse import ONE_OR_MORE
from datetime import datetime
from django.core.cache import cache 
from django.db.models import BooleanField, ExpressionWrapper, Q
from django.db.models.functions import Now
from accounts.models import User

from django.utils import timezone
from pyexpat import model
# from statistics import mode
from django.utils import timezone
from django.urls import reverse
from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    location = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='doctor/', blank=True, null=True)
    address = models.CharField(max_length=60)
    contact = models.BigIntegerField()
    speciality=models.CharField(max_length=60)
    hospital_id = models.ForeignKey('Hospital', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Patient(models.Model):
    gender_category = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=60)
    gender = models.CharField(max_length=20, choices=gender_category)
    contact = models.BigIntegerField()
    details = models.CharField(max_length=150)
    doctor_id = models.ForeignKey('Doctor', on_delete=models.CASCADE)

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
        return super().get_queryset().annotate(expired=ExpressionWrapper(
            Q(valid_to__lt=Now()), output_field=BooleanField()))


class Stock(models.Model):
    category = models.ForeignKey(Category,
                                 null=True,
                                 on_delete=models.CASCADE,
                                 blank=True)
    drug_name = models.CharField(max_length=50, blank=True, null=True)
    drug_color = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    manufacture = models.CharField(max_length=50, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    drug_strength = models.CharField(max_length=10, blank=True, null=True)
    valid_from = models.DateTimeField(blank=True,
                                      null=True,
                                      default=timezone.now)
    valid_to = models.DateTimeField(blank=False, null=True)
    drug_description = models.TextField(blank=True, max_length=1000, null=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    objects = ExpiredManager()

    def __str__(self):
        return str(self.drug_name)


class StoreKipper(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    nid = models.CharField(max_length=50)
    Salary = models.BigIntegerField()
    user_id=models.ForeignKey(User, on_delete=models.CASCADE)

    join_date = models.DateTimeField(auto_now_add='')


class Store(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=50)
    store_kiper = models.ForeignKey('StoreKipper', on_delete=models.CASCADE)
    despense_id = models.ForeignKey('Dispense', on_delete=models.CASCADE)


class Dispense(models.Model):

    store_id = models.ForeignKey(Store, on_delete=models.DO_NOTHING, null=True)
    drug_id = models.ForeignKey(Stock,
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=False)
    dispense_quantity = models.PositiveIntegerField(default='1',
                                                    blank=False,
                                                    null=True)
    taken = models.CharField(max_length=300, null=True, blank=True)
    stock_ref_no = models.CharField(max_length=300, null=True, blank=True)
    instructions = models.TextField(max_length=300, null=True, blank=False)
    dispense_at = models.DateTimeField(auto_now_add=True,
                                       null=True,
                                       blank=True)
    storekipper = models.ForeignKey(StoreKipper,
                                    on_delete=models.DO_NOTHING,
                                    null=True)


disc_choice = (
    ("Rs", "Rs"),
    ("Percent", "%"),
)
mode_choices = (("CASH", "CASH"), ("CREDIT", "CREDIT"), ("BANK", "BANK"))


class Sales(models.Model):
    doc_no = models.IntegerField(blank=True, null=True, db_index=True)
    doc_dt = models.DateField(default=timezone.now)

    mode = models.CharField(max_length=10,
                            choices=mode_choices,
                            default="CASH")
    sale_discount = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        default=0.00,
                                        blank=True)
    sale_disc_type = models.CharField(max_length=10,
                                      choices=disc_choice,
                                      default="Percent")
    sale_adjustment = models.DecimalField(max_digits=6,
                                          decimal_places=2,
                                          default=0.00,
                                          blank=True)
    due_date = models.DateField(null=True, blank=True)

    net_amount = models.DecimalField(max_digits=10,
                                     decimal_places=2,
                                     default=0.00,
                                     blank=True)
    rec_amt = models.DecimalField(max_digits=10,
                                  decimal_places=2,
                                  default=0.00,
                                  blank=True)

    net_cgst = models.DecimalField(max_digits=8,
                                   decimal_places=2,
                                   default=0.00,
                                   blank=True)
    net_sgst = models.DecimalField(max_digits=8,
                                   decimal_places=2,
                                   default=0.00,
                                   blank=True)
    net_gst = models.DecimalField(max_digits=8,
                                  decimal_places=2,
                                  default=0.00,
                                  blank=True)

    due_amt = models.DecimalField(max_digits=6,
                                  decimal_places=2,
                                  default=0.00,
                                  blank=True)

    user_id = models.ForeignKey(StoreKipper,
                                on_delete=models.DO_NOTHING,
                                null=True)
    use_date = models.DateField(null=True, blank=True)

    ref_note = models.CharField(max_length=50, null=True, blank=True)

    class Meta():
        unique_together = ("doc_no", "doc_dt")

    def __str__(self):
        return str(self.id)

    def get_absolute_edit_url(self):
        return reverse("sales:edit", kwargs={"pk": self.pk})

    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})
