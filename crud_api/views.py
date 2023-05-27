# Importar librerías necesarias
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from .models import *
from .serializers import *
import csv


def main(request):
    if request.method == 'POST':
        file = request.FILES['file']
        File.objects.create(file = file)

    with open(file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        print(', '.join(row))
    return render(request, 'index.html')