from rest_framework.viewsets import ModelViewSet
from accounts.models.Account import Account
from accounts.serializers.Account import AccountSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsTransactionOwner


class AccountViewSet(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsTransactionOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
