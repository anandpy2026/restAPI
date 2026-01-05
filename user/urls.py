from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserAPI

router = DefaultRouter()
router.register(r'user', UserAPI)

urlpatterns = [
    path('', include(router.urls)),
]