from django.urls import path
from .views import (
    ProductCreateView,
    StorageCreateView,
    ProductUpdateView,
    StorageUpdateView,
    ProductDeleteView,
    StorageDeleteView,
    ProductDetailView,
    StorageDetailView,
    StorageListView,
    ProductListView,
    testing_func,
    CompanyCreateView,
    CompanyListView,
)

app_name = 'storages'

urlpatterns = [
    # dynamic urls

    # Products url
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("catalog/", ProductListView.as_view(), name="product_list"),

    #
    path("company/new/", CompanyCreateView.as_view(), name="company_new"),
    path("company/", CompanyListView.as_view(), name="company_list"),

    path("<int:pk>/edit", StorageUpdateView.as_view(), name="storage_edit"),
    path("<int:pk>/delete/", StorageDeleteView.as_view(), name="storage_delete"),
    path("<int:pk>/detail", StorageDetailView.as_view(), name="storage_detail"),
    path("create/", StorageCreateView.as_view(), name="storage_new"),
    path("", StorageListView.as_view(), name="storage_list"),
    path("<str:storage>/", testing_func),
]
