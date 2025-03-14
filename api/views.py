from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FarmerTokenSerializer, FarmerKeySerializer
from .models import FarmerToken, FarmerKey



class TokenView(APIView):
    def post(self, request):
        farmer_key = request.body.get('farmer_key')
        if not farmer_key:
            return Response({'error': 'farmer_key is required!'}, status=status.HTTP_400_BAD_REQUEST)
        
        farmer_token = FarmerToken.objects.create(farmer_key=farmer_key)
        return Response(FarmerTokenSerializer(farmer_token).data, status=status.HTTP_201_CREATED)


class GetFarmerKeyView(APIView):
    def get(self, request):
        farmer_key = FarmerKey.objects.create()
        return Response(FarmerKeySerializer(farmer_key).data, status=status.HTTP_201_CREATED)
