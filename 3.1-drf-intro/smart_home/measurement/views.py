# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework import generics
from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer
from rest_framework.response import Response


class SensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all().order_by('id')
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
        return Response(status=200)


class SensorDetailView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    def patch(self, request, pk):
        if request.data.get('name') is not None:
            Sensor.objects.filter(id=pk).update(name=request.data['name'])
        if request.data.get('description') is not None:
            Sensor.objects.filter(id=pk).update(description=request.data['description'])
        return Response(status=200)
    

class MeasurementView(generics.CreateAPIView):
    def post(self, request):
        Measurement(sensor_id=request.data.get('sensor'), temperature=request.data.get('temperature')).save()
        return Response(status=200)

