from django.urls import path

from .views import OrganizationAPIView, ShopUpdate, export_shops_to_csv

urlpatterns = [
    path('api/organizations/', OrganizationAPIView.as_view()),
    path('api/shops/<int:pk>/', ShopUpdate.as_view()),
    path('api/organizations/<int:id>/shops_file/', export_shops_to_csv),
]