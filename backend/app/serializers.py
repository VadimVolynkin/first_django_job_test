from rest_framework import serializers

from .models import Organization, Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('name', 'description', 'shops')
