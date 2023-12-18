# Generated by Django 4.2.8 on 2023-12-11 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterField(
            model_name='articles',
            name='date',
            field=models.DateTimeField(default='2000-01-01 00:00:00', verbose_name='date_of_publication_of_the_article'),
        ),
    ]