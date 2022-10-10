from django.urls import path
from pharmacy import views

urlpatterns = [
    path('hospital/', views.HospitalList.as_view()),
    path('hospital/<int:pk>/', views.HospitalDetail.as_view()),
    path('doctor/', views.DoctorList.as_view()),
    path('doctor/<int:pk>/', views.DoctorDetail.as_view()),
    path('patient/', views.PatientList.as_view()),
    path('patient/<int:pk>/', views.PatientDetail.as_view()),
    path('medicine/', views.MedicineList.as_view()),
    path('medicine/<int:pk>/', views.MedicineDetail.as_view()),
    path('stock/', views.StockList.as_view()),
    path('stock/<int:pk>/', views.StockDetail.as_view()),
    path('storekipeer/', views.StorekipperList.as_view()),
    path('storekipeer/<int:pk>/', views.StoreKipperDetail.as_view()),
    path('store/', views.StoreList.as_view()),
    path('store/<int:pk>/', views.StoreDetail.as_view()),
    
]