from django.test import TestCase
from django.core.validators import ValidationError
from accounts.models.Account import Account
from django.contrib.auth.models import User


class AccountModelTests(TestCase):
    test_username = "Freddie Firestarter"
    test_account_name = "Vacation Fund"

    def setUp(self):

        self.example_user = User.objects.create_user(
            self.test_username, email="Arson@Crime.com")
        Account.objects.create(
            owner=self.example_user, type=Account.SAVINGS, name=self.test_account_name)

    def test_string_representation(self):
        """
        Checks if str(Account) returns the right selfstring
        """
        test_account = Account.objects.get(name=self.test_account_name)
        self.assertEqual(str(test_account),
                         f"{self.test_username}'s {self.test_account_name}")

    def test_validation_fails_on_bad_type(self):
        """
        Checks if the model will fail to validate with an incorrect account type
        """
        account = Account.objects.create(owner=self.example_user,
                                         type="CRE", name=self.test_account_name)
        with self.assertRaises(ValidationError):
            account.full_clean()
