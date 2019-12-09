from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views.User import UserViewSet
from accounts.views.Account import AccountViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('', include(router.urls))
]
