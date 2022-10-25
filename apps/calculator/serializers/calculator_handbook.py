# DRF
from rest_framework import serializers

# Project
from apps.calculator.models import Cridet
from apps.automobile.models import PositionCategory, Car
from apps.calculator.serializers import PaymentModelSezializer


class CreditsCalcSerializer(serializers.ModelSerializer):
    payment = PaymentModelSezializer(source='payments', many=True, read_only=True)

    class Meta:
        model = Cridet
        fields = [
            'month',
            'payment'
        ]


class LeasingCalcSerializer(serializers.ModelSerializer):
    payment = PaymentModelSezializer(source='payments', many=True, read_only=True)

    class Meta:
        model = Cridet
        fields = [
            'month',
            'payment'
        ]


class PositionCreditCalcModelSerializer(serializers.ModelSerializer):
    credits = CreditsCalcSerializer(source='cridets', many=True, read_only=True)

    class Meta:
        model = PositionCategory
        fields = [
            'id',
            'name',
            'credits'
        ]


class PositionLeasingCalcModelSerializer(serializers.ModelSerializer):
    credits = CreditsCalcSerializer(source='cridets', many=True, read_only=True)

    class Meta:
        model = PositionCategory
        fields = [
            'id',
            'name',
            'credits'
        ]


class CarCreditCalcModelSerializer(serializers.ModelSerializer):
    models = PositionCreditCalcModelSerializer(source='positioncategory_set', many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'models'
        ]


class CarLeasingCalcModelSerializer(serializers.ModelSerializer):
    models = PositionLeasingCalcModelSerializer(source='positioncategory_set', many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id',
            'title',
            'models'
        ]
