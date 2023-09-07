from django.test import TestCase
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from restaurant.models import Menu
from django.urls import reverse

class MenuViewTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.menuItem1 = Menu.objects.create(title="Pizza", price=10.99, inventory=20)
        self.menuItem2 = Menu.objects.create(title="Burger", price=5.99, inventory=15)
        self.menuItem3 = Menu.objects.create(title="Salad", price=7.99, inventory=10)
    
    def test_getall(self):
        response = self.client.get(reverse("menuItem"))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)
