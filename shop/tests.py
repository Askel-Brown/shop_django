from django.test import TestCase
from django.contrib.auth.models import User 

from shop.models import Order, Payment, Product, OrderItem


class TestDataBase(TestCase):
    fixtures = [
        'shop/fixtures/mydata.json'
    ]

    def setUp(self):
        self.user = User.objects.get(username='boomee')

    def test_user_exists(self):
        users = User.objects.all()
        users_number = users.count()
        user = users.first()
        self.assertEqual(users_number, 5)
        self.assertEqual(user.username, 'boomee')
        self.assertTrue(user.is_superuser)

    def test_user_check_password(self):
        self.assertTrue(self.user.check_password('27452644'))

