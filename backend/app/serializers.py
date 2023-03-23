from rest_framework import serializers

from .models import Organization, Shop


class ShopSerializer(serializers.Serializer):    
    # class Meta:
    #     model = Shop
    #     fields = '__all__'

    def update(self, instance, validated_data):
        
        print(instance.name)
        print(validated_data)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class OrganizationSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('name', 'description', 'shops')
