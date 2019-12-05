from rest_framework.serializers import ModelSerializer
from accounts.models.Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = AccountSerializer
        fields = ['type', 'balance', 'owner']
