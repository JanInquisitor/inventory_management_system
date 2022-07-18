from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy

from .forms import StorageForm
from .models import Company, Storage, Product


class HomePageView(TemplateView):
    template_name = "storages/home.html"

    def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        return context


class AboutPageView(TemplateView):
    template_name = "storages/about.html"


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'storages/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'storages/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView, FormView):
    model = Product
    template_name = 'storages/product_create.html'
    fields = ['name', 'price', 'upc', 'tags', 'quantity']

    # Ok, entonces despues el formulario esta validado puedo modificar los atributos y los datos que contiene anttes de
    # llamar el metodo super y guardarlo.
    # def form_valid(self, form):
    #     # form.instance.author = self.request.user   / Tengo esto aqui como referencia
    #     form.instance.storage = self.request.storage = Storage()
    #     return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = 'storages/product_edit.html'
    fields = ['name', 'price', 'upc', 'tags', 'quantity']

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'storages/product_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class StorageCreateView(LoginRequiredMixin, CreateView):
    model = Storage
    template_name = 'storages/storage_create.html'
    fields = ['name', 'company']
    success_url = reverse_lazy('storage_list')


class StorageListView(LoginRequiredMixin, ListView):
    model = Storage
    template_name = 'storages/storage_list.html'


class StorageDetailView(LoginRequiredMixin, DetailView):
    model = Storage
    template_name = 'storages/storage_detail.html'


class StorageUpdateView(LoginRequiredMixin, UpdateView):
    model = Storage
    template_name = 'storages/storage_edit.html'
    fields = ['name']


class StorageDeleteView(LoginRequiredMixin, DeleteView):
    model = Storage
    template_name = 'storages/storage_delete.html'
    success_url = reverse_lazy('storage_list')


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'storages/company_create.html'
    fields = ['name']
    success_url = reverse_lazy('company_list')


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'storages/company_list.html'


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = 'storages/company_detail.html'


def testing_func(req):
    return HttpResponse("It worked.")
