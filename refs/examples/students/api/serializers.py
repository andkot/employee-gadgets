from rest_framework import serializers

from ..models import Student


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name']


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
