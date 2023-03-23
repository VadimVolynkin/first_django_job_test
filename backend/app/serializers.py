from rest_framework import serializers

from .models import Organization
from .consumers import ChatConsumer


class ShopSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.address = validated_data.get('address', instance.address)
        instance.index = validated_data.get('index', instance.index)
        instance.is_deleted = validated_data.get('is_deleted', instance.is_deleted)
        instance.save()
        return instance

    def save(self, **kwargs):
        """Добавление в метод save отправки в магазина в вебсокет"""
        consumer = ChatConsumer()
        consumer.connect()
        consumer.receive('{"message": "dssssss"}')
        saved = super().save(**kwargs)
        print("hello world")
        return saved


class OrganizationSerializer(serializers.ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ('name', 'description', 'shops')
