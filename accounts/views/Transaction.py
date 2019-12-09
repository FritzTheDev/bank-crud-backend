from rest_framework.viewsets import ModelViewSet
from accounts.models.Transaction import Transaction
from accounts.serializers.Transaction import TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
