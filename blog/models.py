from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone
# class Category(models.Model):
#     pass

class Blog(models.Model):
    title = models.CharField('タイトル',max_length=50)
    text = MarkdownxField('本文')
    created_at = models.DateTimeField('作成日',default=timezone.now)
    updated_at = models.DateTimeField('更新日',auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title

    def formatted_markdown(self):
        return markdownify(self.text)