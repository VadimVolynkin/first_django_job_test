from django.urls import path

from .views import OrganizationList, ShopUpdate, ExportShopsToCSV, index, room

urlpatterns = [
    path('api/organizations/', OrganizationList.as_view()),
    path('api/shops/<int:pk>/', ShopUpdate.as_view()),
    path('api/organizations/<int:id>/shops_file/', ExportShopsToCSV.as_view()),
    path("chat", index, name="index"),
    path("chat/<str:room_name>/", room, name="room"),
]
