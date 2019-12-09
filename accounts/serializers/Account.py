from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from accounts.models.Account import Account
from accounts.models.Transaction import Transaction


class AccountSerializer(ModelSerializer):
    transactions = PrimaryKeyRelatedField(
        many=True, queryset=Transaction.objects.all())

    class Meta:
        model = Account
        fields = ['type', 'balance', 'owner', 'transactions']
