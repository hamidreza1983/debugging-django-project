from django.shortcuts import render
from .forms import ContactusForm
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Testimonials
from team.models import Team
from services.models import Services
from blogs.models import Blog

# Create your views here.

class HomeView(TemplateView):
    template_name = 'root/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(status=True)
        context["testimonials"] = Testimonials.objects.filter(status=True)
        context["services"] = Services.objects.filter(status=True)[:3]
        context["services2"] = Services.objects.filter(status=True)[:4]
        context["blogs"] = Blog.objects.filter(status=True).order_by("-created_at")[:3]

        return context

class AboutView(TemplateView):
    template_name = 'root/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["teams"] = Team.objects.filter(status=True)
        context["testimonials"] = Testimonials.objects.filter(status=True)
        context["services"] = Services.objects.filter(status=True)[:3]

        return context

def contactus(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "successfully sen message")
            return render(request, 'root/contact.html')
        else:
            messages.add_message(request, messages.ERROR, "data invalid")       
            return render(request, 'root/contact.html')     
    else:
        return render(request, 'root/contact.html')