from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerAPI

router = DefaultRouter()
router.register(r'customer', CustomerAPI)

urlpatterns = [
    path('', include(router.urls)),
]