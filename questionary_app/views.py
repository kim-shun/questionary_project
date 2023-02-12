from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from .forms import GenreCreateForm, QuestionCreateForm
from .models import Genre, Question
from django.db.models import Max


class IndexView(generic.TemplateView):
    template_name = "index.html"


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
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

    if form.is_valid():
        question = Question()
        question.genre = form.cleaned_data['genre']
        question.question_type = form.cleaned_data['question_type']
        question.content = form.cleaned_data['content']
        question.user = request.user

        question_id = 1
        question_order = 1
        if Question.objects.filter(genre=question.genre).exists():
            question_id = Question.objects.all().aggregate(Max('question_id'))["question_id__max"] + 1
            question_order = Question.objects.filter(genre=question.genre).aggregate(Max('question_order'))["question_order__max"] + 1

        Question.objects.create(
            question_id=question_id,
            genre=question.genre,
            question_order=question_order,
            question_type=question.question_type,
            content=question.content,
            user=question.user
        )
        return redirect('questionary_app:index')
    return render(request, 'question_create.html', {'form': form})
