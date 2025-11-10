from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import UsersSerializer, DashboardsSerializer
from .models import Users, Dashboards
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from collections import OrderedDict


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm('app.view_users'):
            return Users.objects.all().order_by('id')
        return Users.objects.none()


class DashboardsViewSet(viewsets.ModelViewSet):
    queryset = Dashboards.objects.all().order_by('id')
    serializer_class = DashboardsSerializer
    permission_classes = [DjangoModelPermissions]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.has_perm('app.view_all_dashboards'):
            return Dashboards.objects.all().order_by('id')
        return Dashboards.objects.filter(
            Q(users=user) | Q(groups__in=user.groups.all())
        ).order_by('id').distinct()

    @action(detail=False, methods=['get'])
    def sectors(self, request):
        queryset = self.get_queryset().order_by('sector', 'title')

        sectors = OrderedDict()
        for dashboard_data in queryset:
            sector = dashboard_data.sector
            if sector not in sectors:
                sectors[sector] = []

            dashboard = {
                'id': dashboard_data.id,
                'title': dashboard_data.title,
            }
            sectors[sector].append(dashboard)

        return Response(sectors)

    @action(detail=True, methods=['get'], url_path='favorite')
    def favorite(self, request, pk=None):
        user = request.user

        try:
            dashboard = Dashboards.objects.get(pk=pk)
        except Dashboards.DoesNotExist:
            return Response({'detail': 'No Dashboards matches the given query.'}, status=status.HTTP_404_NOT_FOUND)

        queryset = self.get_queryset()
        if not queryset.filter(pk=pk).exists():
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)

        if dashboard.fav_by.filter(id=user.id).exists():
            dashboard.fav_by.remove(user)
            return Response({'favorited': False}, status=status.HTTP_200_OK)
        else:
            dashboard.fav_by.add(user)
            return Response({'favorited': True}, status=status.HTTP_200_OK)
