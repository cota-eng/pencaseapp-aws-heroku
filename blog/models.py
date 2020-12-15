from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Blog(models.Model):
    title = models.CharField('タイトル',max_length=50)
    text = MarkdownxField('本文')
    category = models.ForeignKey(Category, related_name="category", on_delete=models.CASCADE)
    meta_description = models.TextField("メタディスクリプション",blank=True)
    created_at = models.DateTimeField('作成日',default=timezone.now)
    updated_at = models.DateTimeField('更新日',auto_now=True, auto_now_add=False)
    is_public = models.BooleanField('公開',default=False)
    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)
    class Meta:
        ordering = ['-created_at']