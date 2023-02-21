from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import GenreCreateForm, QuestionCreateForm
from .models import MGenre, Question, QuestionDetail


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

        Question.objects.create(
            title=question.title,
            user=question.user
        )

        question_id = Question.objects.get(title=question.title)
        question_detail = QuestionDetail()

        for i in range(1, 6):
            question_detail.genre = form.cleaned_data['genre']
            question_order = i
            question_detail.user = request.user
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


class QuestionAnswerView(LoginRequiredMixin, generic.DetailView):
    model = Question
    template_name = 'question_answer.html'
