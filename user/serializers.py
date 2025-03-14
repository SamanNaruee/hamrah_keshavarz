from rest_framework import serializers, generics
from .models import Farmer

class FarmerRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Farmer
        fields = '__all__'
        read_only_fields = ['id', 'created_at']

    def create(self, validated_data):
        user = Farmer.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'],
            email=validated_data['email'],
        )
        return user
    