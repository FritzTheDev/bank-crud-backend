from rest_framework.viewsets import ModelViewSet
from accounts.models.Transaction import Transaction
from accounts.serializers.Transaction import TransactionSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class TransactionViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
