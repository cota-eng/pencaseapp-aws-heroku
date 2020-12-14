from django.urls import path
from .views import BlogListView,BlogDetailView
app_name = "blog"
urlpatterns = [
    path('',BlogListView.as_view(),name="blog"),
    path('<int:pk>/',BlogDetailView.as_view(),name="blog_detail"),
]
