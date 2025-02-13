from django.contrib import admin
from .models import Blog, Comments, Reply, Category, Tag

# Register your models here.
admin.site.register(Blog)
admin.site.register(Comments)
admin.site.register(Reply)
admin.site.register(Category)
admin.site.register(Tag)