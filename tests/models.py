from django.db import models
from articles.models import Articles


class Tests(models.Model):
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    name = models.CharField('test_name', max_length=255, default='Без названия')
    date = models.DateTimeField('date_of_publication_of_the_test', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'


class Questions(models.Model):
    test_id = models.ForeignKey(Tests, on_delete=models.CASCADE)
    text = models.TextField('question_text', default='Пустой вопрос')
    has_several_solutions = models.BooleanField('has_several_solutions', default=False)

    def get_answers(self):
        if self.has_several_solutions:
            answers = self.answers_set.filter(is_right=True).values()
            return [i.get('text') for i in answers]
        else:
            return self.answers_set.filter(is_right=True).first()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'


class Answers(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.TextField('answer_text', default='Пустой ответ')
    is_right = models.BooleanField('is_right', default=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'


class Choices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, on_delete=models.CASCADE)


class Results(models.Model):
    test = models.ForeignKey(Tests, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
