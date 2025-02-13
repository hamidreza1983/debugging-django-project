from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Blog, Comments
from django.core.paginator import Paginator
from .forms import CommentsForm
from django.contrib import messages



# Create your views here.

def blogs(request):
    return render(request, 'blog/blog.html')

class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = "blogs"
    paginate_by = 2

    def get_queryset(self):
        if self.kwargs.get("category"):
            blogs = self.model.objects.filter(category__title=self.kwargs.get("category"))
        elif self.kwargs.get("tag"):
            blogs = self.model.objects.filter(tag__title=self.kwargs.get("tag"))
        else:
            blogs = self.model.objects.filter(status=True)
        return blogs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = 1
        blogs_paginate = Paginator(self.get_queryset(), 2)
        last = blogs_paginate.num_pages
        context["first"] = first
        context["last"] = last
        
        return context


def blog_details(request, id):
    return render(request, 'blog/blog-details.html')

from django.views.generic import DetailView

class BlogDetailsView(DetailView):
    model = Blog
    template_name = 'Blog/blog-details.html'

    def get_context_data(self, **kwargs):
        id = self.kwargs["pk"]
        blog = get_object_or_404(Blog, id=id)
        context = super().get_context_data(**kwargs)
        context["form"] = CommentsForm()
        context["comments"] = Comments.objects.filter(status=True, blog=blog.id)
        context["blogs"] = Blog.objects.filter(status=True).order_by("-created_at")[:5]
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentsForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                id = self.kwargs["pk"]
                blog = get_object_or_404(Blog, id=id)
                comment = form.save(commit=False)
                comment.blog = blog
                comment.save()
                messages.add_message(self.request, messages.SUCCESS, "successfully sent")
                return redirect(self.request.path_info)
            else:
                messages.add_message(request, messages.ERROR, "invalid data")
                return redirect(self.request.path_info)
        else:
            return redirect("accounts:login")
