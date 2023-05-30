from rest_framework import viewsets, permissions, status
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from django.db.models import Avg, Count, Max, Min
from .utils import create_model
from .models import *
from .serializers import *
import pandas as pd

class RestaurantStatisticsViewSet(viewsets.ViewSet):

    serializer = RestaurantSerializer
        
    def list(self, request):
        lat = request.query_params.get('latitude')
        lng = request.query_params.get('longitude')
        radius = request.query_params.get('radius')

        if lat is None or lng is None or radius is None:
            return Response({'error': 'Los parámetros de latitud, longitud y radio son requeridos.'}, status=400)
        
        

        # Lógica para obtener los datos solicitados
        restaurants = Restaurant.objects.filter(
            lat__range=(float(lat) - float(radius), float(lat) + float(radius)),
            lng__range=(float(lng) - float(radius), float(lng) + float(radius))
        )

        count = restaurants.count()
        avg = restaurants.aggregate(Avg('rating'))['rating__avg']
        std = restaurants.aggregate(Count('rating'))['rating__count']
        best = restaurants.aggregate(Max('rating'))['rating__max']
        worst = restaurants.aggregate(Min('rating'))['rating__min']


        return Response({
            'count': count,
            'avg': avg,
            'std': std,
            'best': best,
            'worst': worst
        })

class AllDataView(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RestaurantSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({ 'message' : 'Registro eliminado correctamente'})
        return Response({ 'error' : 'No existe un registro con esos datos'})


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = FileSerializer
    parser_classes = (MultiPartParser,)
    
    def create(self, request):
        file = request.FILES['file']

        obj = File.objects.create(file = file)
        create_model(obj.file)
        return Response({'status': 'success'})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            self.perform_destroy(instance)
            return Response({ 'message' : 'Registro eliminado correctamente'})
        return Response({ 'error' : 'No existe un registro con esos datos'})
      