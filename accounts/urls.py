from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views.User import UserViewSet
from accounts.views.Account import AccountViewSet
from accounts.views.Transaction import TransactionViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('', include(router.urls))
]
