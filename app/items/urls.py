from django.urls import path

from .views import ItemCreateView, ItemDetailView, ItemListView, ItemUpdateView

urlpatterns = [
    path("", ItemListView.as_view(), name="item-list"),
    path("detail/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("edit/<int:pk>/", ItemUpdateView.as_view(), name="item-update"),
    path("add/", ItemCreateView.as_view(), name="item-create"),
]
