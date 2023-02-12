from django import forms

from .models import Genre, Question


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


QUESTION_CHOICE = {
    ('0', '選択タイプ'),
    ('1', 'パーセンテージタイプ')
}


class QuestionCreateForm(forms.ModelForm):
    genre = forms.ModelChoiceField(label="質問のジャンル", queryset=Genre.objects.all())
    question_type = forms.ChoiceField(
        label="質問の形式",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0)

    class Meta:
        model = Question
        fields = ('question_id', 'genre', 'question_order', 'question_type', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
