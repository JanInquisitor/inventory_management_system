from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .models import Company, Storage, Product


class HomePageView(TemplateView):
    template_name = "storages/home.html"


class AboutPageView(TemplateView):
    template_name = "storages/about.html"


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'storages/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'storages/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'storages/product_create.html'
    fields = ["name", "price", "upc", "tags", "quantity"]

    # Ok, entonces despues el formulario esta validado puedo modificar los atributos y los datos que contiene anttes de
    # llamar el metodo super y guardarlo.
    # def form_valid(self, form):
    #     form.instance.author = self.request.user   / Tengo esto aqui como referencia
    #     form.instance.storage = self.request.storage = Storage()
    #     return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'storages/product_edit.html'
    fields = ["name", "price", "upc", "tags", "quantity"]


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'storages/product_delete.html'
    success_url = reverse_lazy("home")


def testing_func(req):
    return HttpResponse("It worked.")
