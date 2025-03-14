from django.urls import path
from .views import TokenView, GetFarmerKeyView

urlpatterns = [
    path('token/', TokenView.as_view(), name='token'),
    path('get-farmer-key/', GetFarmerKeyView.as_view(), name='get_farmer_key'),
]
