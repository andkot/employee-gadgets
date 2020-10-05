from django.http import JsonResponse
from ..models import Model_1
from .serializers import (
    Model_1_ListSerializer,
    Model_1_DetailSerializer,
    Model_1_LoginSerializers,
)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def view_1(request):
    data = Model_1.objects.all()
    response = {'Model_1': list(data.values('id', 'field_1'))}
    return JsonResponse(response)


@api_view(['GET', 'POST'])
def model_1_list(request):
    if request.method == 'GET':
        data = Model_1.objects.all()
        serializer = Model_1_ListSerializer(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Model_1_DetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def model_1_details(request, pk):
    try:
        data = Model_1.objects.get(pk=pk)
    except Model_1.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Model_1_DetailSerializer(data)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Model_1_DetailSerializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        data.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        serializer = Model_1_LoginSerializers(data=request.data)
        # inner_obj = Model_1_LoginSerializers()
        print('aaa')
        if serializer.is_valid():
            print('YES')

            return Response(status=status.HTTP_100_CONTINUE)


            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
