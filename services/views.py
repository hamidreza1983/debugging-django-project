from django.shortcuts import render
from .models import Services
from django.views.generic import TemplateView

# Create your views here.

class ServicesView(TemplateView):
    template_name = 'services/services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["services"] = Services.objects.filter(status=True)[:4]
        context["revservices"] = Services.objects.filter(status=True)[:3]
        return context
    