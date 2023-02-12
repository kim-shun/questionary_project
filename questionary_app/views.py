# import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
# , UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
# from django.shortcuts import get_object_or_404

from .forms import GenreCreateForm, QuestionCreateForm
from .models import Genre, Question


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


class QuestionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Question
    template_name = 'question_create.html'
    form_class = QuestionCreateForm
    success_url = reverse_lazy('questionary_app:index')

    def form_valid(self, form):
        question = form.save(commit=False)
        question.user = self.request.user
        # question.question_order = 99
        # question.question_id = 99
        question.save()
        messages.success(self.request, '質問を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "質問の作成に失敗しました。")
        return super().form_invalid(form)
