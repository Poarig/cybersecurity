from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesList.as_view(), name='articles'),
    path('<int:pk>', views.ArticlesDetailView.as_view(), name='article_detail')
]
