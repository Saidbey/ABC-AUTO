from rest_framework import serializers

from apps.automobile.models.gifts import Gifts


class BonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gifts
        fields = "__all__"
