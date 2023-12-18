# Generated by Django 4.2.8 on 2023-12-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Без названия', max_length=255, verbose_name='article_name')),
                ('text', models.TextField(default='Пустая статья', verbose_name='article_text')),
                ('date', models.DateTimeField(default='2000-01-01 00:00:00[.000]', verbose_name='date_of_publication_of_the_article')),
                ('tests', models.BinaryField(default=b'\x80\x04}\x94.', verbose_name='article_tests')),
            ],
        ),
    ]
