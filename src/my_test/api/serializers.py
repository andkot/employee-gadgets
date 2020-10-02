from rest_framework.serializers import ModelSerializer
from ..models import Model_1

class Model_1_ListSerializer(ModelSerializer):
    class Meta:
        model = Model_1
        fields = ['id']

class Model_1_DetailSerializer(ModelSerializer):
    class Meta:
        model = Model_1
        fields = ['id', 'field_1']

class Model_1_LoginSerializers(ModelSerializer):
    class Meta:
        model = Model_1
        fields = ['id', 'field_1']

