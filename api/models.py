import uuid
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core import validators
from django.conf import settings

class FarmerKey(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)



class FarmerToken(models.Model):
    farmer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    farmer_key = models.CharField(max_length=255)
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.farmer} - {self.created_at} - {self.token}' if self.token else self.farmer.name
    
    def is_valid(self):
        return self.expired_at > datetime.now()
    
    def refresh_token(self):
        self.token = uuid.uuid4()
        self.expired_at = datetime.now() + timedelta(minutes=30)
        self.save()
    
