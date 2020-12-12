from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Article, Comment,Reply
from .forms import CommentCreateForm,ArticleCreateForm,ReplyCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import reverse,resolve_url
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        self.object = self.get_object()
        print(self.object.author)
        return self.request.user == self.object.author

@login_required
def LikeView(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
    else:    
        article.likes.add(request.user)
    return HttpResponseRedirect(reverse("pencaseapp:article_detail",args=[str(pk)]))

class ArticleListView(ListView):
    model = Article
    template_name = "pencaseapp/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["article_trend"] = Article.objects.annotate().order_by('-likes')[:6]
        context["article_latest"] = Article.objects.order_by('-created_at')[:6]
        return context
    
class ArticleRandomListView(ListView):
    model = Article
    template_name = "pencaseapp/random.html"
    ordering = '?'
    paginate_by = 10

class ArticleLikeOrderListView(ListView):
    model = Article
    template_name = "pencaseapp/like.html"
    ordering = 'object.comments.created_at'
    paginate_by = 10

class ArticleUpdateView(OnlyYouMixin, UpdateView):
    model = Article
    template_name = "pencaseapp/article_form.html"
    form_class = ArticleCreateForm
    def get_success_url(self):
        return reverse('pencaseapp:article_detail',kwargs={"pk":self.kwargs['pk']})
    # def get_object(self):
    #     return self.request.user
    def form_valid(self, form):
        return super().form_valid(form)

class ArticleDeleteView(OnlyYouMixin, DeleteView):
    model = Article
    template_name = "pencaseapp/article_delete.html"
    def get_success_url(self):
        return reverse('pencaseapp:home')
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = "pencaseapp/article_form.html"
    form_class = ArticleCreateForm
    login_url = 'accounts:account_login'
    def form_valid(self, form):
        article = form.save(commit=False)
        article.author = self.request.user
        article.save()
        messages.success(self.request,'投稿が完了しました。ありがとうございました。')
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('pencaseapp:article_detail',kwargs={"pk":self.object.pk})

class MyArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "pencaseapp/my_article.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_article"] = Article.objects.filter(author=self.request.user)
        return context
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = "pencaseapp/detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        aim = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = aim.get_total_likes()
        context["total_likes"] = total_likes
        return context
    

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "pencaseapp/comment_form.html"
    redirect_field_name = 'pencaseapp:home'
    login_url = 'accounts:account_login'
    def form_valid(self, form):
        pencase_pk = self.kwargs['pk']
        pencase = get_object_or_404(Article, pk=pencase_pk)
        comment = form.save(commit=False)
        comment.comment_target = pencase
        comment.commentator = self.request.user
        comment.save()
        return redirect('pencaseapp:article_detail',pk=pencase_pk)

class ReplyCreateView(LoginRequiredMixin,CreateView):
    model = Reply
    form_class = ReplyCreateForm
    template_name = "pencaseapp/reply_form.html"
    redirect_field_name = 'pencaseapp:home'
    login_url = 'accounts:account_login'
    def form_valid(self, form):
        comment_pk = self.kwargs['pk']
        comment = get_object_or_404(Comment, pk=comment_pk)
        reply = form.save(commit=False)
        reply.reply_target = comment
        reply.replyer = self.request.user
        reply.save()
        return redirect('pencaseapp:article_detail', pk=comment.comment_target.pk)
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     comment_pk = self.kwargs['pk']
    #     comment = get_object_or_404(Comment, pk=comment_pk)
    #     context['post'] = comment.reply_target
    #     return context