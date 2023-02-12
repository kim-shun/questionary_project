import logging

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import get_object_or_404

from .forms import GenreCreateForm
from .models import Genre


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
