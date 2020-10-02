from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Employee


class EmployeeSerializer(ModelSerializer):
    again_password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['email', 'name', 'password', 'again_password']
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        employee = Employee(
            email=self.validated_data['email'],
            name=self.validated_data['name']
        )

        password = self.validated_data['password']
        again_password = self.validated_data['again_password']

        if password != again_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        employee.set_password(self.validated_data['password'])
        employee.save()
        return employee

    def create(self, validated_data):
        return self.save(self)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance
