from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    # article_detail_view
)

app_name = 'blogs'
urlpatterns = [
    # path('detail/', article_detail_view, name='article-detail'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>', ArticleDetailView.as_view(), name="article-detail"),
    path('create/', ArticleCreateView.as_view(), name="article-create"),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name="article-update"),
    path('<int:id>/delete', ArticleDeleteView.as_view(), name='article-delete'),


]

