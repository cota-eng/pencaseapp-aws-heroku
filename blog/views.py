from django.shortcuts import render
from .models import Blog
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import Http404  

# class OnlySuperUserMixin(UserPassesTestMixin):
#     raise_exception = True
#     def test_func(self):
#         user = self.request.user
#         return  user.is_superuser

class BlogListView(generic.ListView):
    model = Blog
    template_name = "blog/blog.html"
    paginate_by = 9
    ordering = '-created_at'
    queryset = Blog.objects.filter(is_public=True)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    def get_object(self, queryset=None):
        Blog = super().get_object()
        if Blog.is_public :
            return Blog
        else:
            raise Http404