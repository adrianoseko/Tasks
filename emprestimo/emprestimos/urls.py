from django.urls import path
from .views import PropostasListView, PropostasDetailView

urlpatterns = [
    path('propostas/', PropostasListView.as_view(), name='propostas-list'),
    path('propostas/<int:pk>/', PropostasDetailView.as_view(), name='propostas-detail'),
]