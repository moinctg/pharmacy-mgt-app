from audioop import add
from cmath import exp
from xml.dom import ValidationErr
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import *
from django.contrib.auth import authenticate
from datetime import datetime
from main.utils import CustomPagination, get_access_token, get_query
from main.custom_methods import IsAuthenticatedCustom


# Generate Token Manually

#  add user activity 

def add_user_activity(user,action):
    UserActivities.objects.create(
        user_id = user.id,
        email = user.email,
        fullname= user.fullname,
        action=action


    )
    # create user view 
class CreateuserView(ModelViewSet):
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializers
    permisson_classes = (IsAuthenticatedCustom,)

    def create(self,request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid (raise_exception=True)

        CustomUser.objects.create(**valid_request.validated_data)

        add_user_activity(request.user,"added new user")
        return Response(
            {"success": "User created successfully"},
            status=status.HTTP_201_CREATED
        )
    # Login View 
class LoginView(ModelViewSet):
    http_method_names = ['post']
    queryset = CustomUser.objects.all()
    serializer_class = LoginSerializer

    def crate(self , request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid (raise_exception=True)
        new_user = valid_request.validated_data["is_new_user"]
        if new_user:
            user = CustomUser.objects.filter(
                email=valid_request.validated_data["email"]
            )
            if user:
                user = user[0]
                if not user.password:
                    return Response ({"user_id":user.id})
                else:
                    raise Exception("user has password already")
            else:
                    raise Exception("User wiht email not found")
            user = authenticate(
                username= vlaid_request.validated_data["email"],
                password= vlaid_request.validated_data["password",None]

            )

            if not user:
                return Response(
                     {"error":"Invalid email or password "},
                status = status.Http_400_BAD_REQUEST
                )
        access = get_access_token({"user_id":user.id},1)
        user.last_login = datetime.now( )
        user.save()

        add_user_activity(user,'logged in')
        return Response({"access":access})


# update password 
class UpdatePasswordView(ModelViewSet):
    serializer_class = UpdatePasswordSerializer
    http_method_names = ["post"]
    queryset = CustomUser.objects.all()

    def create(self, request):
        valid_request = self.serializer_class(data=request.data)
        valid_request.is_valid(raise_exception=True)

        user = CustomUser.objects.filter(
            id=valid_request.validated_data["user_id"])

        if not user:
            raise Exception("User with id not found")

        user = user[0]

        user.set_password(valid_request.validated_data["password"])
        user.save()

        add_user_activity(user, "updated password")

        return Response({"success": "User password updated"})

class MyView(ModelViewSet):
    serializer_class = CustomUserSerializer
    http_method_names = ["get"]
    queryset = UserActivities.objects.all()
    permission_classes = (IsAuthenticatedCustom, )

    def list(self, request):
        data = self.serializer_class(request.user).data
        return Response(data)

 
class UserActivitiesView(ModelViewSet):
    serializer_class = UserActivitiesSerializer
    http_method_names = ["get"]
    queryset = UserActivities.objects.all()
    permission_classes = (IsAuthenticatedCustom, )
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
                "fullname", "email", "action"
            )
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        
        return results


class UsersView(ModelViewSet):
    serializer_class = CustomUserSerializer
    http_method_names = ["get"]
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticatedCustom, )
    pagination_class = CustomPagination
    
    def get_queryset(self):
        if self.request.method.lower() != "get":
            return self.queryset

        data = self.request.query_params.dict()
        data.pop("page", None)
        keyword = data.pop("keyword", None)

        results = self.queryset.filter(**data, is_superuser=False)

        if keyword:
            search_fields = (
                "fullname", "email", "role"
            )
            query = get_query(keyword, search_fields)
            results = results.filter(query)
        
        return results                                