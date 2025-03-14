from rest_framework import serializers
from api.models import FarmerToken, FarmerKey

class FarmerTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerToken
        fields = '__all__'
        read_only_fields = ['token']

    
class FarmerKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmerKey
        fields = ['key']
        read_only_fields = ['key']
