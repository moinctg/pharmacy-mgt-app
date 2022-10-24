from operator import mod
from secrets import choice
from signal import raise_signal
import turtle
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.utils import timezone


Roles = (('admin','admin'),('creator','creator'),('sale','sale'))

class CustomUserManager(BaseUserManager):

    def create_superuser(self, email, password, **extara_fields):
        extara_fields.setdefault('is_staff',True)
        extara_fields.setdefault('is_superuser',True)
        extara_fields.setdefault('is_active',True)
        if extara_fields.get("is_staf") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if not email:
            raise ValueError("email field is required")
        
        user = self.model(email=email,**extara_fields)
        user.set_password(password)
        user.save()
        return user
       


        




class CustomUser (AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=250, unique=True)
    Role = models.CharField(max_lenght=8,choice=Roles)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    last_login= models.DateTimeField(null=True)
    

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ("create_at",)

class UserActivities (models.Model):
    user = models.ForeignKey(CustomUser,related_name="user_activities",null=True,on_delete=models.SET_NULL)
    email = models.EmailField()
    fullname = models.CharField(max_length=255)
    action = models.TaxtField()
    crate_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ("-crate_at",)
    def __str__(self):
        return f"{self.fullname} {self.action} on {self.crate_at.strftime('%Y-%m-%d %H:%M')}"