from rest_framework import serializers
from ..models import Employee, Device


class EmployeeDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'url',
            "last_login",
            "position",
            "name",
            "email",
            "avatar", ]


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.ImageField(write_only=True, allow_null=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'position', 'avatar', 'password', 'password2', ]

    def create(self, validated_data):
        validated_data.pop('password2')
        return super().create(validated_data)


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
