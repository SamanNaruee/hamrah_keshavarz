from rest_framework.permissions import BasePermission
from .models import FarmerToken
from datetime import datetime

class IsFarmerAuthenticated(BasePermission):
    def has_permission(self, request, view):
        token = request.headers['Authorization']
        if not token or not token.startswith('Bearer '):
            return False
        
        token = token.split('Bearer ')[1]
        is_farmer_token = FarmerToken.objects.filter(token=token, expired_at__gt=datetime.now()).exists()
        return is_farmer_token