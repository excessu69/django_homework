from django.urls import path

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, MeasurementViewSet

router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'measurements', MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('', include(router.urls)),
]
