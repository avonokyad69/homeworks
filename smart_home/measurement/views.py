# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor
from .serializers import MeasurementSerializer, SensorDetailSerializer

class ListCreateAPIView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        serializer = SensorDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class RetrieveUpdateAPIView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        testmodel_object = self.get_object()
        serializer = SensorDetailSerializer(testmodel_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class CreateAPIView(APIView):
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)