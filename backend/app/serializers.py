from rest_framework import serializers
from .models import Users, Dashboards


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['id']


class DashboardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboards
        fields = '__all__'
        read_only_fields = ['id']
