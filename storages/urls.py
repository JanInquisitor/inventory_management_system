from django.urls import path
from .views import ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView, ProductListView, \
    AboutPageView, HomePageView, testing_func

urlpatterns = [
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="product_edit"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("catalog/", ProductListView.as_view(), name="product_list"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("test/", testing_func),
    path("", HomePageView.as_view(), name="home"),
]
