# Generated by Django 4.2.8 on 2023-12-13 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_articles_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='tests',
        ),
    ]
