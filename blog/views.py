from django.shortcuts import render
from .models import Blog
from django.views import generic
class BlogListView(generic.ListView):
    model = Blog
    template_name = "blog/blog.html"
    paginate_by = 9
    ordering = '-created_at'

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"