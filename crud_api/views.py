from django.shortcuts import render, redirect
from .models import *
from .serializers import *
import pandas as pd

def create_db(file_path):
    df = pd.read_csv(file_path)
    print(df)

def main(request):
    try:
      if request.method == "POST":
        file = request.FILES['file']
        obj = File.objects.create(file =file)
        create_db(obj.file)
        return render(request, 'index.html')
    except:
      print('An exception occurred')