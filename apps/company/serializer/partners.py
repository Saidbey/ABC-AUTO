from rest_framework import serializers
from apps.company.model.partners import Partners


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = '__all__'
