from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin
from accounts.models.Account import Account
from accounts.serializers.Account import AccountSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from accounts.permissions import IsAccountOwner


class AccountViewSet(GenericViewSet, RetrieveModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
