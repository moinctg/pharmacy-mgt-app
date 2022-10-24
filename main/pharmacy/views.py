from pharmacy.models import *
from pharmacy.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Hospital 
class HospitalList(APIView):
    """
    List all Hospital List, or create a new Hospital.
    """
    permission_classes = (IsAuthenticated, )
    def get(self, request, format=None):
        hospital = Hospital.objects.all()
        serializer = HospitalSerializer (hospital, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HospitalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HospitalDetail(APIView):
    """
    Retrieve, update or delete a Hospital instance.
    """
    def get_object(self, pk):
        try:
            return Hospital.objects.get(pk=pk)
        except Hospital.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hospital = self.get_object(pk)
        serializer = HospitalSerializer(hospital)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hospital = self.get_object(pk)
        serializer = HospitalSerializer(hospital, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hospital = self.get_object(pk)
        hospital.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DoctorList(APIView):
    """
    List all Doctor List, or create a new Doctor.
    """
    def get(self, request, format=None):
        doctor = Doctor.objects.all()
        serializer = DoctorSerializer (doctor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#  Doctor 
class DoctorDetail(APIView):
    """
    Retrieve, update or delete a Doctor instance.
    """
    def get_object(self, pk):
        try:
            return Doctor.objects.get(pk=pk)
        except Doctor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        doctor = self.get_object(pk)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        doctor = self.get_object(pk)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Patient
class PatientList(APIView):
    """
    List all Patient List, or create a new Patient.
    """
    def get(self, request, format=None):
        doctor = Patient.objects.all()
        serializer = PatientSerializer (doctor, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PatientDetail(APIView):
    """
    Retrieve, update or delete a Patient instance.
    """
    def get_object(self, pk):
        try:
            return Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        patient = self.get_object(pk)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        paitent = self.get_object(pk)
        serializer = PatientSerializer(paitent, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paitent = self.get_object(pk)
        paitent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Medicine
class MedicineList(APIView):
    """
    List all Patient List, or create a new Patient.
    """
    def get(self, request, format=None):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer (medicine, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MedicineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MedicineDetail(APIView):
    """
    Retrieve, update or delete a Patient instance.
    """
    def get_object(self, pk):
        try:
            return Medicine.objects.get(pk=pk)
        except Medicine.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        medicine = self.get_object(pk)
        serializer = MedicineSerializer(medicine, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paitent = self.get_object(pk)
        paitent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class StockList(APIView):
    """
    List all Stock List, or create a new Patient.
    """
    def get(self, request, format=None):
        stock = Stock.objects.all()
        serializer = StockSerializer (stock, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    """
    Retrieve, update or delete a Stock instance.
    """
    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        paitent = self.get_object(pk)
        paitent.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StorekipperList(APIView):
    """
    List all storekipper, or create a new storekipperent.
    """
    def get(self, request, format=None):
        storekipper = StoreKipper.objects.all()
        serializer = StoreKipperSerializer (storekipper, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreKipperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreKipperDetail(APIView):
    """
    Retrieve, update or delete a Storekipper instance.
    """
    def get_object(self, pk):
        try:
            return StoreKipper.objects.get(pk=pk)
        except StoreKipper.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        storekipper = self.get_object(pk)
        serializer = StoreKipperSerializer(storekipper)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        storeKipper = self.get_object(pk)
        serializer = StoreKipperSerializer(storeKipper, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        storekipper = self.get_object(pk)
        storekipper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StoreList(APIView):
    """
    List all storekipper, or create a new storekipperent.
    """
    def get(self, request, format=None):
        store = Store.objects.all()
        serializer = StoreSerializer (store, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetail(APIView):
    """
    Retrieve, update or delete a Store instance.
    """
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        storekipper = self.get_object(pk)
        storekipper.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

