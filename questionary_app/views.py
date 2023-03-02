from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import GenreCreateForm, QuestionCreateForm, AnswerCreateForm
from .models import MGenre, Question, QuestionDetail, Answer, AnswerDetail


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = "index.html"

    def get_queryset(self):
        questions = Question.objects.filter(user=self.request.user).order_by('-created_at')
        return questions


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = MGenre
    template_name = 'genre_create.html'
    form_class = GenreCreateForm
    success_url = reverse_lazy('questionary_app:index')

    def form_valid(self, form):
        genre = form.save(commit=False)
        genre.user = self.request.user
        genre.save()
        messages.success(self.request, 'ジャンルを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "ジャンルの作成に失敗しました。")
        return super().form_invalid(form)


def create_question(request):
    form = QuestionCreateForm(request.POST or None)

# TODO タイトルのユニークのバリデーション
    if form.is_valid():
        question = Question()
        question.title = form.cleaned_data['title']
        question.user = request.user

        question_id = Question.objects.create(
            title=question.title,
            user=question.user
        )

        question_detail = QuestionDetail()
        question_detail.genre = form.cleaned_data['genre']
        question_detail.user = request.user

        for i in range(1, 6):
            question_order = i
            content = 'content' + str(i)
            answer_type = 'answer_type' + str(i)
            question_detail.content = form.cleaned_data[content]
            question_detail.answer_type = form.cleaned_data[answer_type]
            if (len(question_detail.content) != 0) or (len(question_detail.answer_type) != 0):
                create_question_detail(question_id, question_detail.genre, question_order, question_detail.answer_type,
                                       question_detail.content, question_detail.user)

        return redirect('questionary_app:index')
    return render(request, 'question_create.html', {'form': form})


def create_question_detail(question_id, genre, question_order, answer_type,
                           content, user):

    QuestionDetail.objects.create(
        question=question_id,
        genre=genre,
        question_order=question_order,
        answer_type=answer_type,
        content=content,
        user=user
    )


def create_answer(request, question_id):
    form = AnswerCreateForm(request.POST or None)
    question = Question.objects.get(id=question_id)
    params = {
        'form': form,
        'question': question
    }
    if form.is_valid():
        answer = Answer()
        answer.all_score = form.cleaned_data['all_score']
        answer.comment = form.cleaned_data['comment']
        answer.user = request.user

        answer_id = Answer.objects.create(
            question=question,
            all_score=answer.all_score,
            comment=answer.comment,
            user=question.user
        )
 
        answer_detail = AnswerDetail()
        answer_detail.user = request.user
        count = QuestionDetail.objects.filter(question_id=question).count()

        for i in range(1, count + 1):
            score = 'score' + str(i)
            select_type = 'select_type' + str(i)
            score_content = form.cleaned_data[score]
            select_type_content = form.cleaned_data[select_type]
            question_detail_id = 'question_detail_id' + str(i)
            question_detail = request.POST[question_detail_id]
            answer_detail.question_detail = QuestionDetail.objects.get(id=question_detail)
            if (score_content is None or score_content == "") and (len(select_type_content) != 0):
                answer_detail.content = select_type_content
            elif (score_content is not None and score_content != "") and (len(select_type_content) == 0):
                answer_detail.content = score_content

            if (answer_detail.content is not None and answer_detail.content != ""):
                create_answer_detail(question, answer_detail.question_detail, answer_id,
                                     answer_detail.content, answer_detail.user)
        return redirect('questionary_app:index')
    return render(request, 'answer_create.html', params)


def create_answer_detail(question, question_detail_id, answer_id, content, user):

    AnswerDetail.objects.create(
        question=question,
        question_detail=question_detail_id,
        answer=answer_id,
        content=content,
        user=user
    )
