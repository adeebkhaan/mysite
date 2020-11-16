from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
	path('articles/', views.articles, name='index'),
	path('article/<int:article_id>', views.article_details, name="details"),
	path('articles/<int:article_year>', views.articles_by_year, name="articles_by_year"),

]