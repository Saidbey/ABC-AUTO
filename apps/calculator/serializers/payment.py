from rest_framework import serializers

# Project
from apps.calculator.models import Payment, Cridet
from apps.automobile.models import PositionCategory, Car


class PaymentModelSezializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        