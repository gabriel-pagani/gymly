from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import UsersSerializer, DashboardsSerializer
from .models import Users, Dashboards
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


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

    @action(detail=True, methods=['get'], url_path='favorite')
    def favorite(self, request, pk=None):
        user = request.user
        
        queryset = self.get_queryset()
        try:
            dashboard = queryset.get(pk=pk)
        except Dashboards.DoesNotExist:
            return Response({'detail': 'You do not have permission to perform this action.'}, status=status.HTTP_403_FORBIDDEN)
        
        if dashboard.fav_by.filter(id=user.id).exists():
            dashboard.fav_by.remove(user)
            return Response({'favorited': False}, status=status.HTTP_200_OK)
        else:
            dashboard.fav_by.add(user)
            return Response({'favorited': True}, status=status.HTTP_200_OK)
