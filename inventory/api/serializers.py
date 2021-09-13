from . import models
from rest_framework.serializers import ModelSerializer

class SupplierSerializer(ModelSerializer):
    """ Supplier serializer"""
    class Meta:
        model = models.Supplier
        fields = '__all__'


class InventorySerializer(ModelSerializer):
    """Inventory serializer class"""
    class Meta:
        model = models.Inventory
        fields = ['name', 'availability']
        
    def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep['supplier'] = instance.supplied_by.name
            return rep