from django.urls import path

from .views import OrganizationList, ShopUpdate, export_shops_to_csv

urlpatterns = [
    path('api/organizations/', OrganizationList.as_view()),
    path('api/shops/<int:pk>/', ShopUpdate.as_view()),
    path('api/organizations/<int:id>/shops_file/', export_shops_to_csv),
]