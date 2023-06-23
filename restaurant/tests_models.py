from django.test import TestCase
import datetime
from .models import Booking, Menu

# Create your tests here.
#TestCase class
class MenuItemTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name="testname", price=23, menu_item_description="testdesc")

    def test_get_item(self):
        # item = Menu.objects.create(name="IceCream", price=23, menu_item_description="testdesc")
        item = Menu.objects.get(name="testname")
        self.assertEqual(item.name, "testname")
        self.assertEqual(item.price, 23)
        self.assertEqual(item.menu_item_description, "testdesc")


class BookingItemTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(first_name="testname", reservation_date="2023-06-24", reservation_slot=3)

    def test_get_item(self):
        item = Booking.objects.get(first_name="testname")
        self.assertEqual(item.first_name, "testname")
        self.assertEqual(item.reservation_date, datetime.date(2023, 6, 24))
        self.assertEqual(item.reservation_slot, 3)