import uuid
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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
            models.RegexValidator(
                regex=r'^0\d{11}$|^\+98\d{13}$',
                message='phone number must be 11 digits and starts with 0 or 13 digits and starts with +98',
                code='invalid_phone_number'
            )
        ],
    )

    def __str__(self):
        return self.name