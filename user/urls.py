from django.urls import path
from .views import UserAPI

urlpatterns = [
    path('user/', UserAPI.as_view(), name='user-list'),
    path('user/<int:id>/', UserAPI.as_view(), name='user-detail'),
]
