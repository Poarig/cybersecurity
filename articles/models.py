from django.db import models


class Articles(models.Model):
    name = models.CharField('article_name', max_length=255, default='Без названия')
    text = models.TextField('article_text', default='Пустая статья')
    date = models.DateTimeField('date_of_publication_of_the_article', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
