from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, DashboardsViewSet, AuthViewSet

router = DefaultRouter()
router.register(r'auth', AuthViewSet, basename='auth')
router.register(r'users', UsersViewSet)
router.register(r'dashboards', DashboardsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
