from rest_framework.viewsets import ModelViewSet
from accounts.models.Account import Account
from accounts.serializers.Account import AccountSerializer


class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
