from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


from .views import OrganizationList, ShopUpdate, export_shops_to_csv

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('api/organizations/', OrganizationList.as_view()),
    path('api/shops/<int:pk>/', ShopUpdate.as_view()),
    path('api/organizations/<int:id>/shops_file/', export_shops_to_csv),
]


# GET /api/organizations/                    - список организаций с шопами
# PUT /api/shops/{id}/                       - обновление сущности магазина
# GET /organizations/{id}/shops_file/        - файл с расширением xlsx
