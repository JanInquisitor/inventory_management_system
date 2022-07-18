from django import forms
from .models import Storage, Company


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = ("name", "company")


class CompanyStorage(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name',)
