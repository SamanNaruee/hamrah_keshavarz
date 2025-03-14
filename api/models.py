import uuid
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core import validators
from django.core.validators import RegexValidator

class FarmerKey(models.Model):
    key = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    

class Farmer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(
        max_length=20,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^0\d{11}$|^\+98\d{13}$',
                message='phone number must be 11 digits and starts with 0 or 13 digits and starts with +98',
                code='invalid_phone_number'
            )
        ],
    )

    def __str__(self):
        return self.name


class FarmerToken(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
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
    
