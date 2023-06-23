from django.test import TestCase
from restaurant.models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer
import datetime

# Create your tests here.
#TestCase class
class MenuItemTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="testname", price=23, menu_item_description="testdesc")

    def test_serializer(self):
        items = Menu.objects.get(name="testname")
        serialized_item = MenuSerializer(items)
        self.assertEqual(serialized_item.data["name"], "testname")
        self.assertEqual(serialized_item.data["price"], 23)
        self.assertEqual(serialized_item.data["menu_item_description"], "testdesc")

class BookingItemTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="testname", reservation_date="2023-06-24", reservation_slot=3)

    def test_serializer(self):
        items = Booking.objects.get(first_name="testname")
        serialized_item = BookingSerializer(items)
        self.assertEqual(serialized_item.data["first_name"], "testname")
        self.assertEqual(serialized_item.data["reservation_date"], "2023-06-24")
        self.assertEqual(serialized_item.data["reservation_slot"], 3)