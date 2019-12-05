from django.test import TestCase
from accounts.models.Account import Account


class AccountModelTests(TestCase):
    test_account_name = "Vacation Fund"

    def setUp(self):
        Account.objects.create(
            owner=1, type=Account.SAVINGS, name=self.test_account_name)

    def test_string_representation(self):
        test_account = Account.objects.get(name=self.test_account_name)
        self.assertEqual(str(test_account), self.test_account_name)
