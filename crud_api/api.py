from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from .models import *
from .serializers import *


class AllDataView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestaurantSerializer

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [MultiPartParser, JSONParser, ]

    with open(queryset) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(', '.join(row))
        