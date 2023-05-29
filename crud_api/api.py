from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer
from rest_framework.response import Response
from .models import *
from .serializers import *
import csv


class AllDataView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestaurantSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, FileUploadParser, ]

    
        