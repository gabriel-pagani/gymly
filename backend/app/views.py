from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import UsersSerializer, DashboardsSerializer
from .models import Users, Dashboards


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [DjangoModelPermissions]


class DashboardsViewSet(viewsets.ModelViewSet):
    queryset = Dashboards.objects.all().order_by('id')
    serializer_class = DashboardsSerializer
    permission_classes = [DjangoModelPermissions]
