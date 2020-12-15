from django.db import models
from django.conf import settings
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class Article(models.Model):
    origin_image = models.ImageField('サムネイル',upload_to="media/%Y/%m/%d", height_field=None,null=True, width_field=None, max_length=None)
    thumbnail = ImageSpecField(source='origin_image',
                            processors=[ResizeToFill(480,270)],
                            format="JPEG",
                            options={'quality': 90}
                            )
    theme = models.TextField('テーマ')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    pencase = models.TextField("筆箱")
    mechanical_pencil = models.TextField("シャーペン")
    ball_point_pen = models.TextField("ボールペン")
    eraser = models.TextField("消しゴム")
    others = models.TextField("その他")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="article_likes")
    def get_total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.theme
    
class Comment(models.Model):
    comment_text = models.TextField()
    commentator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    comment_target = models.ForeignKey(Article, related_name="comments",on_delete=models.CASCADE)
    def __str__(self):
        return self.text[:10]
    
class Reply(models.Model):
    reply_target = models.ForeignKey(Comment, related_name="replies", on_delete=models.CASCADE)
    replyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    reply_text = models.TextField()
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    def __str__(self):
        return self.text[:10]