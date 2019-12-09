from django.contrib.auth.models import User
from accounts.models.Account import Account
from rest_framework.serializers import PrimaryKeyRelatedField, ModelSerializer


class UserSerializer(ModelSerializer):
    accounts = PrimaryKeyRelatedField(
        many=True, queryset=Account.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'accounts']
