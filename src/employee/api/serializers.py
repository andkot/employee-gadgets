from rest_framework.serializers import ModelSerializer
from ..models import Employee


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['email', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        # exclude = ['password']

    def create(self, validated_data):
        employee = Employee(
            email=validated_data['email'],
            name=validated_data['name']
        )
        employee.set_password(validated_data['password'])
        employee.save()
        return employee


