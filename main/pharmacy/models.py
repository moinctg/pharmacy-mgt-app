from django.db import models
# from django.db.models import BooleanField, ExpressionWrapper, Q
# from django.db.models.functions import Now
from accounts.models import CustomUser
from  accounts.views import add_user_activity

# from django.utils import timezone
# from pyexpat import model
# from statistics import mode
# from django.utils import timezone
# from django.urls import reverse
# from django.db import models


# Create your models here.

class InventoryGroup(models.Model):
    created_by = models.ForeignKey(
        CustomUser, null=True, related_name="inventory_groups",
        on_delete=models.SET_NULL
    )
    name = models.CharField(max_length=100, unique=True)
    belongs_to = models.ForeignKey(
        'self', null=True, on_delete=models.SET_NULL, related_name="group_relations"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_name = self.name

    def save(self, *args, **kwargs):
        action = f"added new group - '{self.name}'"
        if self.pk is not None:
            action = f"updated group from - '{self.old_name}' to '{self.name}'"
        super().save(*args, **kwargs)
        add_user_activity(self.created_by, action=action)

    def delete(self, *args, **kwargs):
        created_by = self.created_by
        action = f"deleted group - '{self.name}'"
        super().delete(*args, **kwargs)
        add_user_activity(created_by, action=action)

    def __str__(self):
        return self.name





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


# class ExpiredManager(models.Manager):

#     def get_queryset(self):
#         return super().get_queryset().annotate(expired=ExpressionWrapper(
#             Q(valid_to__lt=Now()), output_field=BooleanField()))


# class Stock(models.Model):
#     category = models.ForeignKey(Category,
#                                  null=True,
#                                  on_delete=models.CASCADE,
#                                  blank=True)
#     drug_name = models.CharField(max_length=50, blank=True, null=True)
#     drug_color = models.CharField(max_length=50, blank=True, null=True)
#     quantity = models.IntegerField(default='0', blank=True, null=True)
#     receive_quantity = models.IntegerField(default='0', blank=True, null=True)
#     manufacture = models.CharField(max_length=50, blank=True, null=True)
#     last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#     valid_from = models.DateTimeField(blank=True,
#                                       null=True,
#                                       default=timezone.now)
#     valid_to = models.DateTimeField(blank=False, null=True)
#     drug_description = models.TextField(blank=True, max_length=1000, null=True)
#     image = models.ImageField(upload_to='category/', blank=True, null=True)
#     objects = ExpiredManager()

#     def __str__(self):
#         return str(self.drug_name)


class Inventory(models.Model):
    created_by = models.ForeignKey(
        CustomUser, null=True, related_name="inventory_items",
        on_delete=models.SET_NULL
    )
    code = models.CharField(max_length=10, unique=True, null=True)
    photo = models.ImageField(upload_to='Inventory/', blank=True, null=True)
    group = models.ForeignKey(
        InventoryGroup, related_name="inventories", null=True, on_delete=models.SET_NULL
    )
    total = models.PositiveIntegerField()
    remaining = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=255)
    price = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        if is_new:
            self.remaining = self.total

        super().save(*args, **kwargs)

        if is_new:
            id_length = len(str(self.id))
            code_length = 6 - id_length
            zeros = "".join("0" for i in range(code_length))
            self.code = f"BOSE{zeros}{self.id}"
            self.save()

        action = f"added new inventory item with code - '{self.code}'"

        if not is_new:
            action = f"updated inventory item with code - '{self.code}'"

        add_user_activity(self.created_by, action=action)

    def delete(self, *args, **kwargs):
        created_by = self.created_by
        action = f"deleted inventory - '{self.code}'"
        super().delete(*args, **kwargs)
        add_user_activity(created_by, action=action)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Shop(models.Model):
    created_by = models.ForeignKey(
        CustomUser, null=True, related_name="shops",
        on_delete=models.SET_NULL
    )
    address = models.CharField(max_length=200)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-created_at",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.old_name = self.name

    def save(self, *args, **kwargs):
        action = f"added new shop - '{self.name}'"
        if self.pk is not None:
            action = f"updated shp[] from - '{self.old_name}' to '{self.name}'"
        super().save(*args, **kwargs)
        add_user_activity(self.created_by, action=action)

    def delete(self, *args, **kwargs):
        created_by = self.created_by
        action = f"deleted shop - '{self.name}'"
        super().delete(*args, **kwargs)
        add_user_activity(created_by, action=action)

    def __str__(self):
        return self.name



# class Store(models.Model):
#     name = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)
#     contact = models.BigIntegerField()
#     location = models.CharField(max_length=50)
#     store_kiper = models.ForeignKey('StoreKipper', on_delete=models.CASCADE)
#     # despense_id = models.ForeignKey('Dispense', on_delete=models.CASCADE)

# class StoreKipper(models.Model):
#     name = models.CharField(max_length=20)
#     address = models.CharField(max_length=200)
#     contact = models.BigIntegerField()
#     nid = models.CharField(max_length=50)
#     Salary = models.BigIntegerField()
#     # user_id=models.ForeignKey(User, on_delete=models.CASCADE)

#     join_date = models.DateTimeField(auto_now_add='')

# class Dispense(models.Model):


#     drug_id = models.ForeignKey(Stock,
#                                 on_delete=models.SET_NULL,
#                                 null=True,
#                                 blank=False)
#     dispense_quantity = models.PositiveIntegerField(default='1',
#                                                     blank=False,
#                                                     null=True)
#     taken = models.CharField(max_length=300, null=True, blank=True)
#     stock_ref_no = models.CharField(max_length=300, null=True, blank=True)
#     instructions = models.TextField(max_length=300, null=True, blank=False)
#     dispense_at = models.DateTimeField(auto_now_add=True,
#                                        null=True,
#                                        blank=True)

  

    




# disc_choice = (
#     ("Rs", "Rs"),
#     ("Percent", "%"),
# )
# mode_choices = (("CASH", "CASH"), ("CREDIT", "CREDIT"), ("BANK", "BANK"))


# class Sales(models.Model):
#     doc_no = models.IntegerField(blank=True, null=True, db_index=True)
#     doc_dt = models.DateField(default=timezone.now)

#     mode = models.CharField(max_length=10,
#                             choices=mode_choices,
#                             default="CASH")
#     sale_discount = models.DecimalField(max_digits=6,
#                                         decimal_places=2,
#                                         default=0.00,
#                                         blank=True)
#     sale_disc_type = models.CharField(max_length=10,
#                                       choices=disc_choice,
#                                       default="Percent")
#     sale_adjustment = models.DecimalField(max_digits=6,
#                                           decimal_places=2,
#                                           default=0.00,
#                                           blank=True)
#     due_date = models.DateField(null=True, blank=True)

#     net_amount = models.DecimalField(max_digits=10,
#                                      decimal_places=2,
#                                      default=0.00,
#                                      blank=True)
#     rec_amt = models.DecimalField(max_digits=10,
#                                   decimal_places=2,
#                                   default=0.00,
#                                   blank=True)

#     net_cgst = models.DecimalField(max_digits=8,
#                                    decimal_places=2,
#                                    default=0.00,
#                                    blank=True)
#     net_sgst = models.DecimalField(max_digits=8,
#                                    decimal_places=2,
#                                    default=0.00,
#                                    blank=True)
#     net_gst = models.DecimalField(max_digits=8,
#                                   decimal_places=2,
#                                   default=0.00,
#                                   blank=True)

#     due_amt = models.DecimalField(max_digits=6,
#                                   decimal_places=2,
#                                   default=0.00,
#                                   blank=True)

#     user_id = models.ForeignKey(StoreKipper,
#                                 on_delete=models.DO_NOTHING,
#                                 null=True)
#     use_date = models.DateField(null=True, blank=True)

#     ref_note = models.CharField(max_length=50, null=True, blank=True)

#     class Meta():
#         unique_together = ("doc_no", "doc_dt")

#     def __str__(self):
#         return str(self.id)

#     def get_absolute_edit_url(self):
#         return reverse("sales:edit", kwargs={"pk": self.pk})

#     def get_absolute_url(self):
#         return reverse("sales:detail", kwargs={"pk": self.pk})

class Invoice(models.Model):
    created_by = models.ForeignKey(
        CustomUser, null=True, related_name="invoices",
        on_delete=models.SET_NULL
    )
    shop = models.ForeignKey(
        Shop, related_name="sale_shop", null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)

    def delete(self, *args, **kwargs):
        created_by = self.created_by
        action = f"deleted invoice - '{self.id}'"
        super().delete(*args, **kwargs)
        add_user_activity(created_by, action=action)


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(
        Invoice, related_name="invoice_items", on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        Inventory, null=True, related_name="inventory_invoices", 
        on_delete=models.SET_NULL
    )
    item_name = models.CharField(max_length=255, null=True)
    item_code = models.CharField(max_length=20, null=True)
    quantity = models.PositiveIntegerField()
    amount = models.FloatField(null=True)

    def save(self, *args, **kwargs):
        if self.item.remaining < self.quantity:
            raise Exception(f"item with code {self.item.code} does not have enough quantity")

        self.item_name = self.item.name
        self.item_code = self.item.code

        self.amount = self.quantity * self.item.price
        self.item.remaining = self.item.remaining - self.quantity
        self.item.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.item_code} - {self.quantity}"
