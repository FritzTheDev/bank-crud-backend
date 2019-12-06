from rest_framework.serializers import ModelSerializer
from accounts.models.Account import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['type', 'balance', 'owner']
