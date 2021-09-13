from django.urls import path, include
from . import views

urlpatterns = [
    path('inventory/', views.InventoryView.as_view(), name="inventory" ),
    path('inventory/<int:id>/', views.InventoryDetailView.as_view(), name="inventory-detail" ),

]