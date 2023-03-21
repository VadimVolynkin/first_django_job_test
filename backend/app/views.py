from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Organization, Shop
from .serializers import OrganizationSerializer


class OrganizationList(APIView):
    def get(self, request, format=None):
        organizations = Organization.objects.prefetch_related('shops')
        # organizations = Organization.objects.filter(Shop.objects.filter(is_deleted=False))
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT not allowed."})
        
        try:
            instance = Organization.objects.get(pk=pk)
        except Exception:
            return Response({"error": "Object does not exists."})
        
        serializer = OrganizationSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})
        

# def get_organization(request):
#     orgs = Organization.objects.select_related('shops').all()