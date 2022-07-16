from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Company, Storage, Product


class HomePageView(TemplateView):
    template_name = "storages/home.html"


class AboutPageView(TemplateView):
    template_name = "storages/about.html"


class ProductListView(ListView):
    model = Product
    template_name = 'storages/product_list.html'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'storages/product_create.html'
    fields = ["name", "price", "upc", "labels", "quantity"]


class ProductDetailView(DetailView):
    model = Product
    template_name = 'storages/product_detail.html'
