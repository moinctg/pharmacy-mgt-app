from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers import *
from django.contrib.auth import authenticate
from datetime import datetime
from main.utils import CustomPagination, get_access_token, get_query
from main.custom_methods import IsAuthenticatedCusto


from rest_framework.permissions import IsAuthenticated

# Generate Token Manually


