from django.urls import path
from .views import ProductCreateView, ProductDetailView, ProductListView, AboutPageView, HomePageView

urlpatterns = [
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/new/", ProductCreateView.as_view(), name="product_new"),
    path("catalog/", ProductListView.as_view(), name="product_list"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]
