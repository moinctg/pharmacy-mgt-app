from django.urls import path
from pharmacy import views

urlpatterns = [
    path('hospital/', views.HospitalList.as_view()),
    path('hospital/<int:pk>/', views.HospitalDetail.as_view()),
    path('doctor/', views.DoctorList.as_view()),
    path('doctor/<int:pk>/', views.DoctorDetail.as_view()),
    path('patient/', views.PatientList.as_view()),
    path('patient/<int:pk>/', views.PatientDetail.as_view()),
]