from django.shortcuts import render

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import (EmployeeDetailsSerializer,
                          EmployeeListSerializer,
                          EmployeeCreateSerializer,
                          DeviceListSerializer,
                          DeviceDetailsSerializer,
                          EmployeeSerializer,
                          DeviceSerializer, )
from ..models import Employee, Device
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import action


class EmployeeListView(ListAPIView):
    serializer_class = EmployeeListSerializer
    queryset = Employee.objects.all()


class EmployeeDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = EmployeeDetailsSerializer
    queryset = Employee.objects.all()
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if request.data['password2'] != request.data['password']:
            return Response({'Error': 'pas must match'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        return Response(serializer.data)


class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeCreateSerializer
    queryset = Employee.objects.all()

    def create(self, request, *args, **kwargs):
        pas2 = request.data['password2']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if pas2 != request.data['password']:
            return Response({'Error': 'pas must match'}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeviceListView(ListAPIView):
    serializer_class = DeviceListSerializer
    queryset = Device.objects.all()


class DeviceDetailsView(RetrieveUpdateDestroyAPIView):
    serializer_class = DeviceDetailsSerializer
    queryset = Device.objects.all()


class DeviceCreateView(CreateAPIView):
    serializer_class = DeviceDetailsSerializer
    queryset = Employee.objects.all()


# --------------------------------------------------

class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @action(detail=True, methods=['GET'])
    def devices(self, request, pk=None):
        """Does something on single item."""
        queryset = Employee.objects.get(pk=pk)
        devices = Device.objects.filter(current_user=queryset)
        serializer = DeviceSerializer(devices, many=True, context={'request': request})
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmployeeDetailsSerializer

        return super(EmployeeView, self).get_serializer_class()


class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
