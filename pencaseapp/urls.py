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
                    ArticleLatestOrderListView,
                    ArticleLikeOrderListView,
                    MyPageView)

app_name="pencaseapp"
urlpatterns = [
    path('',ArticleListView.as_view(),name="home"),
    path('trend/',ArticleLikeOrderListView.as_view(),name="trend"),
    path('latest/',ArticleLatestOrderListView.as_view(),name="latest"),
    path('random/',ArticleRandomListView.as_view(),name="random"),
    path('mypage/',MyPageView.as_view(),name="mypage"),
    path('pencase/<int:pk>/',ArticleDetailView.as_view(),name="article_detail"),
    path('comment/<int:pk>/',CommentCreateView.as_view(),name="pencase_comment"),
    path('reply/<int:pk>/',ReplyCreateView.as_view(),name="pencase_reply"),
    path('create/',ArticleCreateView.as_view(),name="article_create"),
    path('update/<int:pk>/',ArticleUpdateView.as_view(),name="article_update"),
    path('delete/<int:pk>/',ArticleDeleteView.as_view(),name="article_delete"),
    path('like/<int:pk>/',LikeView,name="article_likes"),
]
