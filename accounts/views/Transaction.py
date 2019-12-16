from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from accounts.models.Transaction import Transaction
from accounts.serializers.Transaction import TransactionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsTransactionOwner


class TransactionViewSet(GenericViewSet, RetrieveModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTransactionOwner]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
