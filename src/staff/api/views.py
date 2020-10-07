from .serializers import (EmployeeDetailsSerializer,
                          EmployeeSerializer,
                          DeviceSerializer, )
from ..models import Employee, Device
from .permissions import IsOwnerOrReadOnly
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.authentication import BasicAuthentication


class EmployeeView(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

    @action(detail=True, methods=['GET'])
    def devices(self, request, pk=None):
        """Does something on single item."""
        queryset = Employee.objects.get(pk=pk)
        devices = Device.objects.filter(current_user=queryset)
        serializer = DeviceSerializer(devices, many=True, context={'request': request})
        for item in serializer.data:
            del item['current_user']
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EmployeeDetailsSerializer

        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        # must improve !!!
        result = dict(serializer.data)
        result['available devices'] = f'{serializer.data["url"]}devices'
        del result['url']
        return Response(result)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        for elem in serializer.data:
            elem['available devices'] = f'{elem["url"]}devices/'
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if request.data['password2'] != request.data['password']:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.data['password2'] != request.data['password']:
            return Response(status=status.HTTP_403_FORBIDDEN)
        instance = self.get_object()
        res = {}
        for elem in request.data:
            if request.data[str(elem)]:
                res[str(elem)] = request.data[str(elem)]
        # print(OrderedDict([(key, result[key]) for key in result if result[key] is not None]))
        serializer = self.get_serializer(instance, data=res, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)


class DeviceView(ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        current = self.get_serializer(instance)
        last_user = current.data['current_user']
        res = {}
        for elem in request.data:
            if request.data[str(elem)]:
                res[str(elem)] = request.data[str(elem)]
        res['last_user'] = last_user
        serializer = self.get_serializer(instance, data=res, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)

        return Response(serializer.data)
