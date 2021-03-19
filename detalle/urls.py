from django.urls import path
from .views import DetalleListView, DetalleDetailView


urlpatterns = [
    path('nota/<int:pk>/', DetalleDetailView.as_view(), name='detalleDetalle'),
    path('', DetalleListView.as_view(), name='home')
]