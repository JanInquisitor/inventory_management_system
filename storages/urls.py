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

    # fixed urls
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("storage/<int:pk>/edit", StorageUpdateView.as_view(), name="storage_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("storage/<int:pk>/delete/", StorageDeleteView.as_view(), name="storage_delete"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("storage/<int:pk>", StorageDetailView.as_view(), name="storage_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("storage/new/", StorageCreateView.as_view(), name="storage_new"),
    path("company/new/", CompanyCreateView.as_view(), name="company_new"),
    path("company/", CompanyListView.as_view(), name="company_list"),
    path("storage/", StorageListView.as_view(), name="storage_list"),
    path("catalog/", ProductListView.as_view(), name="product_list"),
    path("test/", testing_func),
]
