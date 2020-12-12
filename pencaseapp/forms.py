from django import forms
from .models import Comment,Article,Reply

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('comment_target','commentator',)
        widgets = {
            'text':forms.Textarea(attrs={'class':'form-control'})
        }

class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ('replyer','created_at','reply_target',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Reply'
                })
        }


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'created_at', 'updated_at', 'likes',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'gfdgdfgdgfdgdfg'
                }),
            # ''
        }