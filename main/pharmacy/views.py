from pharmacy.models import Hospital,Doctor,Patient
from pharmacy.serializers import HospitalSerializer,DoctorSerializer,PatientSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Hospital 
class HospitalList(APIView):
    """
    List all Hospital List, or create a new Hospital.
    """
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

