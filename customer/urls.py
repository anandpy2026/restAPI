from django.urls import path
from .views import CustomerAPI

urlpatterns = [
    path('customer/', CustomerAPI.as_view(), name='uscustomerer-list'),
    path('customer/<int:id>/', CustomerAPI.as_view(), name='usecustomerr-detail'),
]

