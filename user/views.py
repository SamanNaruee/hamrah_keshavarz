from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FarmerRegisterSerializer
from .models import Farmer


class FarmerRegisterView(APIView):
    def post(self, request):
        serializer = FarmerRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
