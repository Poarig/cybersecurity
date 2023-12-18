from .models import Articles
from tests.models import Tests
from django.views.generic import DetailView, ListView


class ArticlesList(ListView):
    model = Articles
    template_name = 'articles/articles.html'
    context_object_name = 'articles'


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = "articles/detail_view.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tests'] = Tests.objects.filter(article_id=self.kwargs['pk'])
        return context