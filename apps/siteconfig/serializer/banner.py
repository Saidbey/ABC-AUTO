from rest_framework import serializers
from apps.siteconfig.model.banner import Banner


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
