from rest_framework.serializers import ModelSerializer
from accounts.models.Transaction import Transaction


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['type', 'account', 'amount', 'transaction_datetime']
