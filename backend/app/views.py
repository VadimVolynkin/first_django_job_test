import csv
from django.http import HttpResponse
from django.http import Http404
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .services.email_tasks import send_email
from .models import Organization, Shop
from .serializers import OrganizationSerializer, ShopSerializer

from django.shortcuts import render


def index(request):
    return render(request, "app/index.html")


def room(request, room_name):
    return render(request, "app/room.html", {"room_name": room_name})


class OrganizationList(ListAPIView):
    from django.db.models import Prefetch
    shops = Shop.objects.filter(is_deleted=False)
    queryset = Organization.objects.prefetch_related(
        Prefetch('shops', queryset=shops))
    serializer_class = OrganizationSerializer


# class ShopUpdate(UpdateAPIView):
#     """Обновление сущности магазина
#     с отправкой email
#     """
#     queryset = Shop.objects.all()
#     serializer_class = ShopSerializer
#     lookup_field = 'pk'

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object(id=kwargs['id'])
#         serializer = self.get_serializer(instance, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # Отправка Письма
#             send_email()
#             return Response({"message": "Shop updated successfully"})
#         else:
#             return Response({"message": "failed",
#                              "details": serializer.errors})
            

# # TODO Эта вьюха не показывает поля экземпляра
class ShopUpdate(APIView):

    def get_object(self, pk):
        try:
            return Shop.objects.get(pk=pk)
        except Shop.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        instance = self.get_object(pk)
        serializer = ShopSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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
