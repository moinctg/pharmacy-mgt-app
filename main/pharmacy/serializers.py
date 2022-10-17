from rest_framework import serializers
# from pharmacy.serializers import *
from .models import *
       


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = "__all__"
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
class CategoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
class DispanarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispanary
        fields = "__all__"
class StoreKipperSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreKipper
        fields = "__all__"
class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"