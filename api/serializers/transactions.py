import datetime

from django.db.models import Q

from rest_framework import serializers, viewsets
from rest_framework.fields import SerializerMethodField
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from gasolinestation.models import Transactions, GasolineStation, FuelPrices


class TransactionSerializer(serializers.ModelSerializer):
    fuel = serializers.SlugRelatedField(slug_field="name", queryset=FuelPrices.objects.all(), allow_null=True, required=False)
    gas_station_assigned = serializers.SlugRelatedField(slug_field="name", queryset=GasolineStation.objects.all(), allow_null=True, required=False)
    fuel_name = SerializerMethodField()
    fuel_price = SerializerMethodField()

    class Meta:
        model = Transactions
        fields = "__all__"

    def get_fuel_name(self, obj):
        return "%s" % (obj.fuel.type_of_fuel.name)

    def get_fuel_price(self, obj):
        return "%s" % (obj.fuel.price)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        today = datetime.date.today()

        if self.request.user.position == 'Cashier':
            sales = Transactions.objects.all()
            qs = sales.filter(Q(created_at=today))
            return qs
        elif self.request.user.position == 'Manager':
            sales = Transactions.objects.all()
            return sales
        elif self.request.user.position == 'Owner':
            sales = Transactions.objects.all()
            return sales

    def perform_create(self, serializer):
        cashier = self.request.user.position == 'Cashier'
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if cashier:
            return serializer.save(created_by=self.request.user.full_name)
        elif manager:
            return serializer.save(created_by=self.request.user.full_name)
        elif owner:
            return serializer.save(created_by=self.request.user.full_name)

    def perform_update(self, serializer):
        cashier = self.request.user.position == 'Cashier'
        manager = self.request.user.position == 'Manager'
        owner = self.request.user.position == 'Owner'

        if cashier:
            return serializer.save(updated_by=self.request.user.full_name)
        elif manager:
            return serializer.save(updated_by=self.request.user.full_name)
        elif owner:
            return serializer.save(updated_by=self.request.user.full_name)