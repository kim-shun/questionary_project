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


class QuestionCreateForm(forms.Form):
    title = forms.CharField(label='アンケートのタイトル', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1', 'placeholder': '例：東京都の住みやすさ'}), required=True)
    genre = forms.ModelChoiceField(label="アンケートのジャンル", queryset=MGenre.objects.all(), required=True)
    content1 = forms.CharField(label='質問内容1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=True)
    content2 = forms.CharField(label='質問内容2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    content3 = forms.CharField(label='質問内容3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    content4 = forms.CharField(label='質問内容4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    content5 = forms.CharField(label='質問内容5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item1_1 = forms.CharField(label='選択肢1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item1_2 = forms.CharField(label='選択肢2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item1_3 = forms.CharField(label='選択肢3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item1_4 = forms.CharField(label='選択肢4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item1_5 = forms.CharField(label='選択肢5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item2_1 = forms.CharField(label='選択肢1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item2_2 = forms.CharField(label='選択肢2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item2_3 = forms.CharField(label='選択肢3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item2_4 = forms.CharField(label='選択肢4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item2_5 = forms.CharField(label='選択肢5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item3_1 = forms.CharField(label='選択肢1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item3_2 = forms.CharField(label='選択肢2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item3_3 = forms.CharField(label='選択肢3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item3_4 = forms.CharField(label='選択肢4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item3_5 = forms.CharField(label='選択肢5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item4_1 = forms.CharField(label='選択肢1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item4_2 = forms.CharField(label='選択肢2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item4_3 = forms.CharField(label='選択肢3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item4_4 = forms.CharField(label='選択肢4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item4_5 = forms.CharField(label='選択肢5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item5_1 = forms.CharField(label='選択肢1', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item5_2 = forms.CharField(label='選択肢2', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item5_3 = forms.CharField(label='選択肢3', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item5_4 = forms.CharField(label='選択肢4', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)
    choice_item5_5 = forms.CharField(label='選択肢5', widget=forms.Textarea(attrs={'cols': '80', 'rows': '1'}), required=False)


ANSWER_CHOICE = (
    ('very applicable', 'とてもあてはまる'),
    ('applicable', 'あてはまる'),
    ('somewhat applicable', 'ややあてはまる'),
    ('neutrality', 'どちらとも言えない'),
    ('somewhat not applicable', 'ややあてはまらない'),
    ('not applicable', 'あてはまらない'),
    ('not applicable at all', '全くあてはまらない')
)


class AnswerCreateForm(forms.Form):
    select_type1 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial='applicable',
        required=False
    )
    select_type2 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial='applicable',
        required=False
    )
    select_type3 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial='applicable',
        required=False
    )
    select_type4 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial='applicable',
        required=False
    )
    select_type5 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial='applicable',
        required=False
    )
    score1 = forms.IntegerField(label='点数', initial="80",
                                widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                required=False)
    score2 = forms.IntegerField(label='点数', initial="80",
                                widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                required=False)
    score3 = forms.IntegerField(label='点数', initial="80",
                                widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                required=False)
    score4 = forms.IntegerField(label='点数', initial="80",
                                widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                required=False)
    score5 = forms.IntegerField(label='点数', initial="80",
                                widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                required=False)
    all_score = forms.IntegerField(label='総合点', initial="80",
                                   widget=forms.NumberInput(attrs={'min': 0, 'max': 100}),
                                   required=True)
    comment = forms.CharField(label='自由コメント', widget=forms.Textarea, required=False)
