import csv

from django.core.mail import send_mail
from django.http import HttpResponse
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, Shop
from .serializers import OrganizationSerializer, ShopSerializer

# class OrganizationList(ListAPIView):
#     queryset = Organization.objects.all()
#     serializer_class = OrganizationSerializer


class OrganizationAPIView(APIView):

    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response({"organizations": serializer.data})


class ShopUpdate(UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Shop updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})

    # def put(self):
    #     """Отправка email"""
    #     send_mail(
    #         'Subject here',
    #         'Here is the message.',
    #         'from@example.com',
    #         ['to@example.com'],
    #         fail_silently=False)
    #     return HttpResponse('Message was send')


def export_shops_to_csv(request, id: int):
    """Экспорт Магазинов в csv

    Args:
        id организации

    Returns:
        csv файл
    """
    
    shops = Shop.objects.filter(organization_id=id)
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=shops.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['id', 'name', 'description', 'address', 'index', 'is_deleted'])
    shops = shops.values_list(
        'id', 'name', 'description', 'address', 'index', 'is_deleted')
    for shop in shops:
        writer.writerow(shop)
    return response