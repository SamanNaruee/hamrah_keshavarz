from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FarmerTokenSerializer
from .models import FarmerToken
from django.shortcuts import get_object_or_404


class TokenView(APIView):
    def get(self, request):
        farmer_key = request.query_params['farmer_key']
        if not farmer_key:
            return Response({'error': 'farmer_key is required!'}, status=status.HTTP_400_BAD_REQUEST)
        
        farmer_token = get_object_or_404(FarmerToken, farmer__id=farmer_key)
        if not farmer_token.is_valid():
            farmer_token.refresh_token()
        
        return Response(FarmerTokenSerializer(farmer_token).data)

