from django.test import TestCase
from restaurant.models import MenuItem
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        MenuItem.objects.create(title='Pabellón', price=55.90, featured=True)
        MenuItem.objects.create(title='Platanitos', price=10.50, featured=False)
        MenuItem.objects.create(title='Cachapa', price=45.00, featured=True)

    def test_getall(self):
        # Initialize the test client
        client = APIClient()

        # Send a GET request to the Menu API endpoint
        response = client.get('/restaurant/menu/')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Retrieve all Menu objects from the database
        menus = MenuItem.objects.all()

        # Serialize the Menu objects
        serializer = MenuItemSerializer(menus, many=True)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)