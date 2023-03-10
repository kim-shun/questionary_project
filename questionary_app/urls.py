from django.urls import path
from . import views

app_name = 'questionary_app'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('genre-create/', views.GenreCreateView.as_view(), name="genre_create"),
    path('question-create/', views.create_question, name="question_create"),
    path('answer-create/<int:question_id>/', views.create_answer, name="answer_create"),
    path('answer-detail/<int:question_id>/', views.answer_detail, name="answer_detail"),
]
