from rest_framework import serializers

from ..models import Employee, Device


class EmployeeListSerializer(serializers.HyperlinkedModelSerializer):
    # serializers.HyperlinkedIdentityField
    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', ]


class EmployeeDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "last_login",
            "position",
            "name",
            "email",
            "avatar", ]


class EmployeeCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = [
            'url',
            "position",
            "name",
            "email",
            "avatar",
            "password",
            'password2', ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data.pop('password2')
        return super(EmployeeCreateSerializer, self).create(validated_data)


class DeviceListSerializer(serializers.HyperlinkedModelSerializer):
    # current_user = serializers.HyperlinkedRelatedField(queryset=Employee.objects.all(), )

    class Meta:
        model = Device
        fields = ['name', 'current_user', ]


class DeviceDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


# --------------------------------------------------

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    avatar = serializers.ImageField(write_only=True, allow_null=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'avatar', 'password', 'password2', ]

    def create(self, validated_data):
        validated_data.pop('password2')
        return super(EmployeeSerializer, self).create(validated_data)


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
