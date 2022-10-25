from rest_framework import serializers
from apps.automobile.models.company import CarCompany


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCompany
        fields = "__all__"
