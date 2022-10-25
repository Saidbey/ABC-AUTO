from rest_framework import serializers
from apps.company.model.address import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'




