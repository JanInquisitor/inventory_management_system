from django.views.generic import TemplateView, ListView

from storages.models import Storage


class HomePageView(TemplateView):
    model = Storage
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
