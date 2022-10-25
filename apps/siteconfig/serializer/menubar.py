from rest_framework import serializers
from apps.siteconfig.model.menubar import MenuBar


class MenyBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuBar
        fields = '__all__'
