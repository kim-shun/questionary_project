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
    ('scoreType', '点数形式(例：95点)'),
    ('selectType', '選択形式(あてはまる/どちらとも言えない/あてはまらない)'),
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

    choice_item1_1 = forms.CharField(label='選択肢1', required=False)
    choice_item1_2 = forms.CharField(label='選択肢2', required=False)
    choice_item1_3 = forms.CharField(label='選択肢3', required=False)
    choice_item1_4 = forms.CharField(label='選択肢4', required=False)
    choice_item1_5 = forms.CharField(label='選択肢5', required=False)
    # choice_item1_list = [choice_item1_1, choice_item1_2, choice_item1_3, choice_item1_4, choice_item1_5]
    choice_item2_1 = forms.CharField(label='選択肢1', required=False)
    choice_item2_2 = forms.CharField(label='選択肢2', required=False)
    choice_item2_3 = forms.CharField(label='選択肢3', required=False)
    choice_item2_4 = forms.CharField(label='選択肢4', required=False)
    choice_item2_5 = forms.CharField(label='選択肢5', required=False)
    # choice_item2_list = (choice_item2_1, choice_item2_2, choice_item2_3, choice_item2_4, choice_item2_5)
    choice_item3_1 = forms.CharField(label='選択肢1', required=False)
    choice_item3_2 = forms.CharField(label='選択肢2', required=False)
    choice_item3_3 = forms.CharField(label='選択肢3', required=False)
    choice_item3_4 = forms.CharField(label='選択肢4', required=False)
    choice_item3_5 = forms.CharField(label='選択肢5', required=False)
    choice_item4_1 = forms.CharField(label='選択肢1', required=False)
    choice_item4_2 = forms.CharField(label='選択肢2', required=False)
    choice_item4_3 = forms.CharField(label='選択肢3', required=False)
    choice_item4_4 = forms.CharField(label='選択肢4', required=False)
    choice_item4_5 = forms.CharField(label='選択肢5', required=False)
    choice_item5_1 = forms.CharField(label='選択肢1', required=False)
    choice_item5_2 = forms.CharField(label='選択肢2', required=False)
    choice_item5_3 = forms.CharField(label='選択肢3', required=False)
    choice_item5_4 = forms.CharField(label='選択肢4', required=False)
    choice_item5_5 = forms.CharField(label='選択肢5', required=False)


ANSWER_CHOICE = {
    ('correct', 'あてはまる'),
    ('neutral', 'どちらとも言えない'),
    ('incorrect', 'あてはまらない')
}


class AnswerCreateForm(forms.Form):
    select_type1 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    select_type2 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    select_type3 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    select_type4 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
        required=False
    )
    select_type5 = forms.ChoiceField(
        choices=ANSWER_CHOICE,
        widget=forms.RadioSelect,
        initial=0,
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
