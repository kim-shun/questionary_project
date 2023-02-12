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


class QuestionCreateForm(forms.ModelForm):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())

    class Meta:
        model = Question
        fields = ('question_id', 'genre', 'question_order', 'question_type', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
