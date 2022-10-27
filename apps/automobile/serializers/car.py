from rest_framework import serializers

from apps.automobile.models import Car, CarLikes


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarLikes
        fields = '__all__'
