from django.urls import path
from .views import FarmerRegisterView


urlpatterns = [
    path('register/', FarmerRegisterView.as_view(), name='register'),
]