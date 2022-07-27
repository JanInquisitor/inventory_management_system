from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin, View
from django.views.generic.edit import ModelFormMixin

from .models import Company, Storage, Product


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


# NOTE: I could check with this view a `selected` storage or something like that...
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'storages/product_list.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'storages/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'storages/product_create.html'
    fields = ['name', 'price', 'upc', 'tags', 'quantity']

    # def get_form_kwargs(self):
    #     kw = super(ProductCreateView, self).get_form_kwargs()
    #     kw['request'] = self.request
    #     print(kw)
    #     return kw

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


# ==== Test classes ====
class SelectedStorage(ModelFormMixin, ContextMixin, View):

    def get_form_kwargs(self):
        kw = super(SelectedStorage, self).get_form_kwargs()
        kw['request'] = self.request
        return kw


def testing_func(request, storage, **kwargs):
    print(storage)
    return HttpResponse("It worked.")
