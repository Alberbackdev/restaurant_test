
from django.urls import path, include
from rest_framework import routers
from .views import AllDataView, FileViewSet, RestaurantStatisticsViewSet

router = routers.DefaultRouter()
router.register(r'alldata', AllDataView, basename='alldata')
router.register(r'files', FileViewSet, 'file')
router.register(r'restaurants/statistics', RestaurantStatisticsViewSet, basename='restaurant-statistics')

urlpatterns = [
    path('api/', include(router.urls)),
]
