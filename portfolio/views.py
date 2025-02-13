from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import Portfolio
from .models import Category
from team.models import Team

# Create your views here.
class PortfolioListView(ListView):
    model = Portfolio
    template_name = "portfolio/portfolio.html"
    context_object_name = "portfolios"
    paginate_by = 6  

    def get_queryset(self):
        qs = Portfolio.objects.filter(status=True).order_by("-created_at")
        category = self.request.GET.get("category")
        if category:
            qs = qs.filter(category__title__iexact=category)  
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/portfolio-details.html"
    context_object_name = "portfolio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        agent = self.object.agent  
        context["agent"] = agent
        context["agent_skill"] = agent.skill 
        context["all_agents"] = Team.objects.all() 
        return context