from django.contrib import admin
from .models import Blog
from markdownx.admin import MarkdownxModelAdmin
admin.site.register(Blog, MarkdownxModelAdmin)