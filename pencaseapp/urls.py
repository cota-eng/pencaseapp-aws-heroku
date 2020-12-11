from django.urls import path
from .views import (ArticleListView,
                    ArticleDetailView,
                    CommentCreateView,
                    ArticleCreateView,
                    ArticleUpdateView,
                    ArticleDeleteView,
                    LikeView,
                    ArticleRandomListView,
                    ReplyCreateView,
                    MyArticleListView)

app_name="pencaseapp"
urlpatterns = [
    path('',ArticleListView.as_view(),name="home"),
    # path('trend/',.as_view(),name="order_by_like"),
    # path('latest/',.as_view(),name="order_by_created_at"),
    path('random/',ArticleRandomListView.as_view(),name="random"),
    path('myarticle/',MyArticleListView.as_view(),name="my_article"),
    path('detail/<int:pk>/',ArticleDetailView.as_view(),name="article_detail"),
    path('comment/<int:pk>/',CommentCreateView.as_view(),name="pencase_comment"),
    path('reply/<int:pk>/',ReplyCreateView.as_view(),name="pencase_reply"),
    path('create/',ArticleCreateView.as_view(),name="article_create"),
    path('update/<int:pk>/',ArticleUpdateView.as_view(),name="article_update"),
    path('delete/<int:pk>/',ArticleDeleteView.as_view(),name="article_delete"),
    path('like/<int:pk>/',LikeView,name="article_likes"),
]
