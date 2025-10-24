from rest_framework import serializers
from .models import Users, Plans, Contracts, Payments


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        read_only_fields = ['id']


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = '__all__'
        read_only_fields = ['id']


class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = '__all__'
        read_only_fields = ['id']


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'
        read_only_fields = ['id']
