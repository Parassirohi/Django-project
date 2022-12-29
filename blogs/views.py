from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .forms import ArticleForm

from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .models import Article
# Create your views here.


def article_detail_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():

        form.save()

    context = {
        "form": form
    }
    return render(request, 'article/article_detail.html', context)


class ArticleListView(ListView):
    template_name = 'article/article_list.html'

    queryset = Article.objects.all()  # <blogs>/<modelname>_list.html


class ArticleDetailView(DetailView):
    template_name = "article/article_detail_2.html"
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    form_class = ArticleForm
    template_name = 'article/article_create.html'
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ArticleUpdateView(UpdateView):
    form_class = ArticleForm
    template_name = "article/article_create.html"
    queryset = Article.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = "article/article_delete.html"
    # success_url = "/blogs/"

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blogs:article-list')


