from rest_framework import serializers
from apps.company.model.about import AboutCompany, Filials


class AboutCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = '__all__'


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filials
        fields = '__all__'
