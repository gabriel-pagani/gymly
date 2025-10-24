from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, PlansViewSet, ContractsViewSet, PaymentsViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'plans', PlansViewSet)
router.register(r'contracts', ContractsViewSet)
router.register(r'payments', PaymentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
