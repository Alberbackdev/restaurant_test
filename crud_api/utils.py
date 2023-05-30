from .models import *
from .serializers import *
import pandas as pd

def create_model(file_path):
  df = pd.read_csv(file_path, delimiter=',')
  print(df.values)
  register_list = [list(row) for row in df.values]

  for l in register_list:
      Restaurant.objects.create(
          id = l[0], 
          rating = l[1],
          name = l[2],
          site = l[3],
          email = l[4],
          phone = l[5],
          street = l[6],
          city = l[7],
          state = l[8],
          lat = l[9],
          lng = l[10]
      )