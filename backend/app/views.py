import csv

from . services.email_tasks import send_email
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Organization, Shop
from .serializers import OrganizationSerializer, ShopSerializer


class OrganizationList(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ShopUpdate(UpdateAPIView):
    """Обновление сущности магазина"""
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object(id=kwargs['id'])
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Отправка Письма
            send_email()
            return Response({"message": "Shop updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})


# class ShopUpdate(APIView):

#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})

#         try:
#             instance = Shop.objects.get(pk=pk)
#         except Exception:
#             return Response({"error": "Object does not exists"})

#         serializer = ShopSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response({"shop": serializer.data})


# TODO стоит ли выносить эту логику в сервис
class ExportShopsToCSV(APIView):
    """Экспорт Магазинов в csv"""

    def get(self, request, id: int):
        """Экспорт Магазинов в csv

        Args:
            id организации

        Returns:
            csv файл
        """
        response = HttpResponse('text/csv')
        response['Content-Disposition'] = 'attachment; filename=shops.csv'
        writer = csv.writer(response)
        shops = Shop.objects.filter(organization_id=id)
        writer.writerow(
            ['id', 'name', 'description', 'address', 'index', 'is_deleted'])
        shops = shops.values_list(
            'id', 'name', 'description', 'address', 'index', 'is_deleted')
        for shop in shops:
            writer.writerow(shop) 
        return response
