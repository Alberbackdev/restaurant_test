
from django.urls import path, include
from rest_framework import routers
from .api import AllDataView, FileViewSet

router = routers.DefaultRouter()
router.register(r'alldata', AllDataView, 'alldata')
router.register(r'files', FileViewSet, 'file')

urlpatterns = [
    path('api/', include(router.urls)),
]
