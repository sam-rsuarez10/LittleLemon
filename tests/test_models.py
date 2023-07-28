from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):
    def test_create_menu(self):
        menu = Menu.objects.create(title='French Fries', price=50.0, inventory=20)
        self.assertEqual(menu.__str__(), 'French Fries : 50.0')