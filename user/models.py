from django.db import models
from django.core.validators import RegexValidator
import uuid
from django.contrib.auth.models import AbstractUser

class Farmer(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
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
