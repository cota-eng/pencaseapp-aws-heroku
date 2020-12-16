from django import forms
from .models import Comment,Article,Reply

class ProtectSpamForm(forms.CharField):
    """override Field"""
    
    def __init__(self, label="荒らし対策",**kwargs):
        super().__init__(required=True, label=label,**kwargs)
        self.widget.attrs['placeholder'] = '「ふでばこ」を漢字に変換してください。'
    def clean(self, value):
        value = super().clean(value)
        if value == '筆箱':
            return value
        else:
            raise forms.ValidationError('違います。')

class CommentCreateForm(forms.ModelForm):

    captha = ProtectSpamForm(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    class Meta:
        model = Comment
        exclude = ('created_at','comment_target', 'commentator',)
        widgets = {
            'comment_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '相手を傷つけないように注意しましょう。\n※自分の投稿にはコメントできません。'
                })
        }
        labels = {
            'comment_text':'感想を入力してください。'
        }


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        exclude = ('replyer','created_at','reply_target',)
        widgets = {
            'reply_text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder':'返事を記入してください。'
                })
        }
        labels = {
            'reply_text':'返事'
        }


class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ('author', 'created_at', 'updated_at', 'likes')
        labels = {
            'thumbnail':'サムネイル'
        }
        widgets = {
            'theme': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '自分の筆箱のテーマを入力してください。',
                'rows':'5'
                }),
            'pencase': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'自分の筆箱の解説をしてください。\n書くことがなければ、「なし」などと記入してください。\n例えば、使っている筆箱は、ユナイテッドビーズのバトンペンケースです。'
                }),
            'mechanical_pencil': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'自分のシャーペンの解説をしてください。\n書くことがなければ、「なし」などと記入してください。\n例えば、使っているシャーペンは、s20とクルトガアドバンスなどです。\ns20の良いところは...です。\nでも、値段が少し高いので扱いには注意しています。'
                }),
            'ball_point_pen': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'自分のボールペンの解説をしてください。\n書くことがなければ、「なし」などと記入してください。\n例えば、使っているボールペンは、ゼブラのサラサがほとんどです。\n買いやすく、発色もいいので気に入っています。'
                }),
            'eraser': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'自分の消しゴムの解説をしてください。\n書くことがなければ、「なし」などと記入してください。\n例えば、無難にMONOを使っています。\n折れやすいのが嫌ですが、安くて消しやすいです。'
                }),
            'others': forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'その他の文房具の解説をしてください。\n書くことがなければ、「なし」などと記入してください。\n例えば、定規はアルミアンドウッド定規、シャー芯はハイユニがお気に入りです。'
                }),
        }