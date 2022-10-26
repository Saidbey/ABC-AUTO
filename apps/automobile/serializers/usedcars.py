from rest_framework import serializers
from apps.automobile.models.usedcars import Usedcars


class UsedCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usedcars
        fields = "__all__"
