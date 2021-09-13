from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from  django.views.generic.detail import DetailView
from api.models import Inventory

class InventoryView(ListView):
    model = Inventory
    template_name = 'inventory_list.html'


class InventoryDetailView(DetailView):
    """Detail view"""
    model = Inventory
    template_name = "inventory_details.html"
    pk_url_kwarg = 'id'
