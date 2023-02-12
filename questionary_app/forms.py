from django import forms
from .models import Genre


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('genre',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


QUESTION_CHOICE = {
    ('selectType', '選択タイプ'),
    ('percentageType', 'パーセンテージタイプ')
}


class QuestionCreateForm(forms.Form):
    genre = forms.ModelChoiceField(
        label="質問のジャンル",
        queryset=Genre.objects.all(),
        required=True
    )

    question_type = forms.ChoiceField(
        label="質問の形式",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=True
    )

    content = forms.CharField(
        label='質問内容',
        required=True
    )