from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views.User import UserViewSet

router = DefaultRouter()
router.register(r'snippets', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
