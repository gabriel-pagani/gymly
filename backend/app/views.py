from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions
from .serializers import UsersSerializer, PlansSerializer, ContractsSerializer, PaymentsSerializer
from .models import Users, Plans, Contracts, Payments


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('id')
    serializer_class = UsersSerializer
    permission_classes = [DjangoModelPermissions]


class PlansViewSet(viewsets.ModelViewSet):
    queryset = Plans.objects.all().order_by('id')
    serializer_class = PlansSerializer
    permission_classes = [DjangoModelPermissions]


class ContractsViewSet(viewsets.ModelViewSet):
    queryset = Contracts.objects.all().order_by('id')
    serializer_class = ContractsSerializer
    permission_classes = [DjangoModelPermissions]


class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all().order_by('id')
    serializer_class = PaymentsSerializer
    permission_classes = [DjangoModelPermissions]
