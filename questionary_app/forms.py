from django import forms
from .models import MGenre


class GenreCreateForm(forms.ModelForm):
    class Meta:
        model = MGenre
        fields = ('genre_name', )

    def __init__(self,  *args,  **kwargs):
        super().__init__(*args,  **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


QUESTION_CHOICE = {
    ('scoreType', '点数形式'),
    ('selectType', '選択形式(◯△×)'),
    ('customSelectType', 'カスタム選択形式')
}


class QuestionCreateForm(forms.Form):
    title = forms.CharField(label='質問のタイトル', required=True)
    genre = forms.ModelChoiceField(label="質問のジャンル", queryset=MGenre.objects.all(), required=True)
    content1 = forms.CharField(label='質問内容1', required=True)
    content2 = forms.CharField(label='質問内容2', required=False)
    content3 = forms.CharField(label='質問内容3', required=False)
    content4 = forms.CharField(label='質問内容4', required=False)
    content5 = forms.CharField(label='質問内容5', required=False)
    answer_type1 = forms.ChoiceField(
        label="回答の形式1",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=True
    )
    answer_type2 = forms.ChoiceField(
        label="回答の形式2",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    answer_type3 = forms.ChoiceField(
        label="回答の形式3",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    answer_type4 = forms.ChoiceField(
        label="回答の形式4",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    answer_type5 = forms.ChoiceField(
        label="回答の形式5",
        choices=QUESTION_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )

