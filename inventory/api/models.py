from django.db import models

# Create your models here.

class BaseModel(models.Model):
    """Base model for creating all models"""
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        if hasattr(self, 'name'):
            return self.name
        else:
            return self.created

class Supplier(BaseModel):
    """Supplier model"""
    name = models.CharField(max_length=64, db_index=True)

    class Meta:
        db_table = 'supplier'
        ordering = ['-created']


class Inventory(BaseModel):
    name = models.CharField(max_length=32, db_index=True)
    description = models.CharField(max_length=256)
    note = models.CharField(max_length=100, null=True, blank=True)
    stock = models.IntegerField(default=0)
    availability = models.BooleanField(default=False)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='supplier')

    class Meta:
        db_table = 'inventory'
        ordering = ['-created']