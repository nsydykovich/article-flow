from django.http import HttpResponse
from django.template import loader

from articles.models import Article


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def articles(request):
    all_articles = Article.objects.all().values()
    template = loader.get_template('articles/all_articles.html')
    context = {
        'articles': all_articles,
    }
    return HttpResponse(template.render(context, request))
