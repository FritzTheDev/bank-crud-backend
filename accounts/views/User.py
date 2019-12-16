from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import User
from accounts.serializers.User import UserSerializer
from accounts.permissions import IsUser


class UserViewSet(ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
