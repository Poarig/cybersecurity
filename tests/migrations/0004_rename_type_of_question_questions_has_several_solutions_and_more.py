# Generated by Django 4.2.8 on 2023-12-15 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0003_rename_question_id_questions_test_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='type_of_question',
            new_name='has_several_solutions',
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct', models.IntegerField(default=0)),
                ('wrong', models.IntegerField(default=0)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.tests')),
            ],
        ),
        migrations.CreateModel(
            name='Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.answers')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.questions')),
            ],
        ),
    ]
