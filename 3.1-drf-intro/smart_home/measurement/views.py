# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer
from rest_framework.decorators import action

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def retrieve(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = SensorDetailSerializer(sensor)
        return Response(serializer.data)

class MeasurementViewSet(viewsets.ViewSet):
    def create(self, request):
        sensor_id = request.data.get('sensor')
        temperature = request.data.get('temperature')

        try:
            sensor = Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return Response({'detail': 'Датчик не найден.'}, status=status.HTTP_404_NOT_FOUND)

        measurement = Measurement(sensor=sensor, temperature=temperature)
        measurement.save()
        return Response({'status': 'Измерение добавлено.'}, status=status.HTTP_201_CREATED)
