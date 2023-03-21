from rest_framework.generics import UpdateAPIView, ListAPIView

from .models import Organization, Shop
from .serializers import OrganizationSerializer, ShopSerializer


class OrganizationList(ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ShopUpdate(UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


def export_shops_to_csv(request, id):
    from django.http import HttpResponse
    import csv
    shops = Shop.objects.filter(organization_id=id)
    response = HttpResponse('text/csv')
    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    writer.writerow(
        ['id', 'name', 'description', 'address', 'index', 'is_deleted'])
    shops = shops.values_list(
        'id', 'name', 'description', 'address', 'index', 'is_deleted')
    for shop in shops:
        writer.writerow(shop)
    return response
    