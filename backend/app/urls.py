from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, DashboardsViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'dashboards', DashboardsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
