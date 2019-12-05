from django.test import TestCase
from accounts.models.Account import Account
from django.contrib.auth.models import User


class AccountModelTests(TestCase):
    test_account_name = "Vacation Fund"

    def setUp(self):
        example_user = User.objects.create_user(
            "Freddie Firestarter", email="Arson@Crime.com")
        Account.objects.create(
            owner=example_user, type=Account.SAVINGS, name=self.test_account_name)

    def test_string_representation(self):
        test_account = Account.objects.get(name=self.test_account_name)
        self.assertEqual(str(test_account), self.test_account_name)
