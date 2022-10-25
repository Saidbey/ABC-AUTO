from rest_framework import serializers

# Projects
from apps.calculator.serializers.calculator_handbook import CarCreditCalcModelSerializer, CarLeasingCalcModelSerializer


class CalculateSerializer(serializers.Serializer):
    credit = CarCreditCalcModelSerializer(many=True, read_only=True)
    leasing = CarLeasingCalcModelSerializer(many=True, read_only=True)
