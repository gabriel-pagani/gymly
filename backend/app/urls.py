from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, DashboardsViewSet, logout_view

router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'dashboards', DashboardsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('logout/', logout_view, name='logout'),
]
