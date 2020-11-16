from django.shortcuts import render
from .models import *

# Create your views here.
def articles(request):
	articles = Article.objects.all()
	return render(request, 'news/articles.html',{
		'articles':articles,
		})

def article_details(request, article_id):
	article_details = Article.objects.get(pk=article_id)
	return render(request, 'news/article_details.html', {
		'article_details':article_details,
		})
def articles_by_year(request, article_year):
	articles_by_year = Article.objects.filter(date__year=article_year)
	return render(request, 'news/articles_by_year.html', {
		'articles_by_year':articles_by_year,
		'article_year':article_year,
		})