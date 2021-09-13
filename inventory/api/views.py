from rest_framework import generics
from . import serializers
from . import models
# Create your views here.

class InventoryView(generics.ListAPIView):
    """Inventory list view"""
    serializer_class = serializers.InventorySerializer

    def get_queryset(self):
        queryset = models.Inventory.objects.all()
        inventory_name = self.request.query_params.get('name', None)
        if inventory_name:
            queryset = queryset.filter(name__contains=inventory_name)
        return queryset