from django.test import TestCase
from api.models import Inventory, Supplier
from django.urls import reverse


class InventoryListViewTest(TestCase):
    "testcases for testing inventory view"

    @classmethod
    def setUpTestData(cls) -> None:
        supplier = Supplier.objects.create(name = 'test1')
        for i in range(10):
            inventory = Inventory.objects.create(
                name=f"product {i}",
                description=f"description {i}",
                supplied_by= supplier
            )
        return super().setUpTestData()

    def test_url_exists(self):
        resp = self.client.get('/inventory/')
        self.assertEqual(resp.status_code, 200)
    
    def test_url_template(self):
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'inventory_list.html')

    def test_inventory_details_url(self):
        inventory_obj = Inventory.objects.all()[:2]
        for obj in inventory_obj:
            resp = self.client.get(f'/inventory/{obj.pk}/')
            self.assertEqual(resp.status_code, 200)