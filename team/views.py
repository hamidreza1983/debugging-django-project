from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Team

# Create your views here.

class TeamsView(TemplateView):
    template_name = 'team/team.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(status=True)
        return context