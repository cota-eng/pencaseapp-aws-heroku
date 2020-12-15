from django.contrib import admin
from .models import Blog,Category
from markdownx.admin import MarkdownxModelAdmin
admin.site.register(Blog, MarkdownxModelAdmin)
admin.site.register(Category)