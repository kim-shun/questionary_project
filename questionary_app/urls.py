from django.urls import path
from . import views

app_name = 'questionary_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('genre-create/', views.GenreCreateView.as_view(), name="genre_create"),
    path('question-create/', views.create_question, name="question_create"),
    path('question-answer/<int:pk>/', views.QuestionAnswerView.as_view(), name="question_answer"),
    path('answer-create/<int:question_id>/', views.create_answer, name="answer_create"),
]
