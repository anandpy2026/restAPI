from django.urls import path
from .views import AgentAPI

urlpatterns = [
    path('agent/', AgentAPI.as_view(), name='agent-list'),
    path('agent/<int:id>/', AgentAPI.as_view(), name='agent-detail'),
]
