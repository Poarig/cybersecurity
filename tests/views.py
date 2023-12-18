from .models import Tests, Questions, Answers, Choices, Results
from articles.models import Articles
from django.db.models import F
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse


class TestsList(ListView):
    model = Tests
    template_name = 'tests/tests.html'
    context_object_name = 'tests'


class TestsDetailView(DetailView):
    model = Tests
    template_name = "tests/detail_view.html"
    context_object_name = "test"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Articles.objects.get(pk=Tests.objects.get(id=self.kwargs['pk']).id)
        return context


def display_test(request, test_id):
    request.session['correct'] = 0
    request.session['wrong'] = 0

    test = get_object_or_404(Tests, pk=test_id)
    question = test.questions_set.first()

    return redirect(reverse('display_question',
                            kwargs={'test_id': test_id,
                                    'question_id': question.pk}))


def display_question(request, test_id, question_id):
    test = get_object_or_404(Tests, pk=test_id)
    questions = test.questions_set.all()
    current_question, next_question = None, None

    for ind, question in enumerate(questions):
        if question.pk == question_id:
            current_question = question
            if ind != len(questions) - 1:
                next_question = questions[ind + 1]

    context = {'test': test,
               'question': current_question,
               'next_question': next_question}

    return render(request, 'tests/display.html', context)


def grade_question(request, test_id, question_id):
    question = get_object_or_404(Questions, pk=question_id)

    try:
        if question.has_several_solutions:
            correct_answer = question.get_answers()
            answers_ids = request.POST.getlist('answer')
            user_answers = []
            if answers_ids:
                for answer_id in answers_ids:
                    user_answer = Answers.objects.get(pk=answer_id)
                    user_answers.append(user_answer.text)

                is_correct = correct_answer == user_answers

                if is_correct is True:
                    request.session['correct'] += 1
                else:
                    request.session['wrong'] += 1

        elif not question.has_several_solutions:
            correct_answer = question.get_answers()
            user_answer = question.answers_set.get(pk=request.POST['answer'])

            is_correct = correct_answer == user_answer

            if is_correct is True:
                request.session['correct'] += 1
            else:
                request.session['wrong'] += 1

    except:
        return render(request, 'tests/partial.html',
            {'question': question})

    return render(
        request, 'tests/partial.html',
        {'is_correct': is_correct,
         'correct_answer': correct_answer,
         'question': question})


def test_results(request, test_id):
    test = get_object_or_404(Tests, pk=test_id)
    questions = test.questions_set.all()
    correct = request.session['correct']
    wrong = request.session['wrong']
    context = {'quiz': test,
               'correct': correct,
               'wrong': wrong,
               'number': len(questions),
               'skipped': len(questions) - (correct + wrong)}

    return render(request, 'tests/results.html', context)
