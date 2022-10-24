from pharmacy.models import *
from pharmacy.serializers import *
from django.http import Http404
from rest_framework.viewSets import ModelViewSet
from rest_framework.response import Response
from main.custom_methods import IsAuthenticatedCustom
from main.utils import CustomPagination , get_query
from django.db.models import Count, Sum, F
from django.db.models.functions import Coalesce, TruncMonth
from accounts.views import add_user_activity
from accounts.models import CustomUser
import csv
import codecs

class InventoryView(ModelViewSet):
    queryset = Inventory.objects.select_related("group", "created_by")
    serializer_class = InventorySerializer
    permission_classes = (IsAuthenticatedCustom,)
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data)

        if keyword:
            search_fields = (
                "code", "created_by__fullname", "created_by__email", 
                "group__name", "name"
            )
            query = get_query(keyword, search_fields)
            return results.filter(query)
        
        return results


    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id":request.user.id})
        return super().create(request, *args, **kwargs)

class InventoryGroupView(ModelViewSet):
    queryset = InventoryGroup.objects.select_related(
        "belongs_to", "created_by").prefetch_related("inventories")
    serializer_class = InventoryGroupSerializer
    permission_classes = (IsAuthenticatedCustom,)
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data)

        if keyword:
            search_fields = (
                "created_by__fullname", "created_by__email", "name"
            )
            query = get_query(keyword, search_fields)
            results = results.filter(query)

        
        
        return results.annotate(
            total_items = Count('inventories')
        )

    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id":request.user.id})
        return super().create(request, *args, **kwargs)


class ShopView(ModelViewSet):
    queryset = Shop.objects.select_related("created_by")
    serializer_class = ShopSerializer
    permission_classes = (IsAuthenticatedCustom,)
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data)

        if keyword:
            search_fields = (
                "created_by__fullname", "created_by__email", "name"
            )
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        
        return results

    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id":request.user.id})
        return super().create(request, *args, **kwargs)


class InvoiceView(ModelViewSet):
    queryset = Invoice.objects.select_related(
        "created_by", "shop").prefetch_related("invoice_items")
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticatedCustom,)
    pagination_class = CustomPagination

    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data)

        if keyword:
            search_fields = (
                "created_by__fullname", "created_by__email", "shop__name"
            )
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        
        return results

    def create(self, request, *args, **kwargs):
        request.data.update({"created_by_id":request.user.id})
        return super().create(request, *args, **kwargs)


class SummaryView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedCustom,)
    queryset = InventoryView.queryset

    def list(self, request, *args, **kwargs):
        total_inventory = InventoryView.queryset.filter(
            remaining__gt=0
        ).count()
        total_group = InventoryGroupView.queryset.count()
        total_shop = ShopView.queryset.count()
        total_users = CustomUser.objects.filter(is_superuser=False).count()

        return Response({
            "total_inventory": total_inventory,
            "total_group": total_group,
            "total_shop": total_shop,
            "total_users": total_users
        })


class SalePerformanceView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedCustom,)
    queryset = InventoryView.queryset

    def list(self, request, *args, **kwargs):
        query_data = request.query_params.dict() 
        total = query_data.get('total', None)
        query = self.queryset

        if not total:
            start_date = query_data.get("start_date", None)
            end_date = query_data.get("end_date", None)

            if start_date:
                query = query.filter(
                    inventory_invoices__created_at__range=[start_date, end_date]
                )

        items = query.annotate(
            sum_of_item=Coalesce(
                Sum("inventory_invoices__quantity"), 0
            )
        ).order_by('-sum_of_item')[0:10]

        response_data = InventoryWithSumSerializer(items, many=True).data
        return Response(response_data)


class SaleByShopView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedCustom,)
    queryset = InventoryView.queryset

    def list(self, request, *args, **kwargs):
        query_data = request.query_params.dict() 
        total = query_data.get('total', None)
        monthly = query_data.get('monthly', None)
        query = ShopView.queryset

        if not total:
            start_date = query_data.get("start_date", None)
            end_date = query_data.get("end_date", None)

            if start_date:
                query = query.filter(
                    sale_shop__created_at__range=[start_date, end_date]
                )

        if monthly:
            shops = query.annotate(month=TruncMonth('created_at')).values(
                'month', 'name').annotate(amount_total=Sum(
                    F("sale_shop__invoice_items__quantity") * 
                    F("sale_shop__invoice_items__amount")
                ))

        else:
            shops = query.annotate(amount_total=Sum(
                    F("sale_shop__invoice_items__quantity") * 
                    F("sale_shop__invoice_items__amount")
                )).order_by("-amount_total")

        response_data = ShopWithAmountSerializer(shops, many=True).data
        return Response(response_data)


class PurchaseView(ModelViewSet):
    http_method_names = ('get',)
    permission_classes = (IsAuthenticatedCustom,)
    queryset = InvoiceView.queryset

    def list(self, request, *args, **kwargs):
        query_data = request.query_params.dict() 
        total = query_data.get('total', None)
        query = InvoiceItem.objects.select_related("invoice", "item")

        if not total:
            start_date = query_data.get("start_date", None)
            end_date = query_data.get("end_date", None)

            if start_date:
                query = query.filter(
                    created_at__range=[start_date, end_date]
                )

        query = query.aggregate(
            amount_total=Sum(F('amount') * F('quantity')), total=Sum('quantity')
            )

        return Response({
            "price": "0.00" if not query.get("amount_total") else query.get("amount_total"),
            "count": 0 if not query.get("total") else query.get("total"),
        })


class InventoryCSVLoaderView(ModelViewSet):
    http_method_names = ('post',)
    queryset = InventoryView.queryset
    permission_classes = (IsAuthenticatedCustom,)
    serializer_class = InventorySerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.FILES['data']
        except Exception as e:
            raise Exception("You need to provide inventory CSV 'data'")

        inventory_items = []

        try:
            csv_reader = csv.reader(codecs.iterdecode(data, 'utf-8'))
            for row in csv_reader:
                if not row[0]:
                    continue
                inventory_items.append(
                    {
                        "group_id": row[0],
                        "total": row[1],
                        "name": row[2],
                        "price": row[3],
                        "photo": row[4],
                        "created_by_id": request.user.id
                    }
                )
        except csv.Error as e:
            raise Exception(e)

        if not inventory_items:
            raise Exception("CSV file cannot be empty")

        data_validation = self.serializer_class(data=inventory_items, many=True)
        data_validation.is_valid(raise_exception=True)
        data_validation.save()

        return Response({"success": "Inventory items added successfully"})


# Hospital 
class Hospitalview(ModelViewSet):
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

