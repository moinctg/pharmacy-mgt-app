
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser,PermissionsMixin
    )

#  Roles Create 

Roles = (('admin','admin'),('creator','creator'),('sale','sale'))


class CustomUserManager(BaseUserManager):

     def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        if not email:
            raise ValueError("Email field is required")

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
       


        

class CustomUser (AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(max_length=250, unique=True)
    role = models.CharField(max_length=8, choices=Roles)
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

class UserActivities(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name="user_activities", null=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    fullname = models.CharField(max_length=255)
    action = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at", )

    def __str__(self):
        return f"{self.fullname} {self.action} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"