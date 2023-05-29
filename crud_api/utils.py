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

""" def create_from_csv(file):
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        id = row[0], 
        rating = row[1],
        name = row[2],
        site = row[3],
        email = row[4],
        phone = row[5],
        street = row[6],
        city = row[7],
        state = row[8],
        lat = row[9],
        lng = row[10]
        pass
 """