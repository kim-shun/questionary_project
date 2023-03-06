from accounts.models import CustomUser
from django.db import models


class MGenre(models.Model):
    """質問ジャンルマスタモデル"""

    genre_name = models.CharField(verbose_name='質問ジャンル名', max_length=60, null=False, unique=True)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'MGenre'
        db_table = 'genre'

    def __str__(self):
        return self.genre_name


class Question(models.Model):
    """質問テーブルモデル"""

    title = models.CharField(verbose_name='タイトル', max_length=60, null=False, unique=True)
    genre = models.ForeignKey(MGenre, verbose_name="質問ジャンル",
                              related_name='question_genre', on_delete=models.PROTECT, null=False)
    answer_num = models.PositiveIntegerField(verbose_name="回答人数", null=False, default=0)
    answer_count = models.PositiveIntegerField(verbose_name="回答件数", null=False, default=0)
    median_score = models.PositiveIntegerField(verbose_name="総合点中央値", null=False, default=0)
    average_score = models.PositiveIntegerField(verbose_name="総合点平均値", null=False, default=0)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Question'
        db_table = 'question'


class QuestionDetail(models.Model):
    """質問詳細テーブルモデル"""

    question = models.ForeignKey(Question, verbose_name='質問ID',
                                 related_name='question_detail', on_delete=models.PROTECT, null=False)
    question_order = models.PositiveIntegerField(verbose_name="質問順序", null=False, default=1)
    answer_type = models.CharField(verbose_name='回答形式', max_length=20, null=False)
    content = models.TextField(verbose_name='質問内容', null=False)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'QuestionDetail'
        db_table = 'question_detail'

        constraints = [
            models.UniqueConstraint(fields=['question', 'question_order'],
                                    name='unique_question_detail'),
        ]

    def __str__(self):
        return self.question


class Answer(models.Model):
    """回答テーブルモデル"""

    question = models.ForeignKey(Question, verbose_name='質問ID',
                                 related_name='question_answer', on_delete=models.PROTECT, null=False)
    all_score = models.PositiveIntegerField(verbose_name="総合点", null=False, default=0)
    comment = models.TextField(verbose_name='自由コメンt', null=True)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Answer'
        db_table = 'answer'


class AnswerDetail(models.Model):
    """回答詳細テーブルモデル"""
    question = models.ForeignKey(Question, verbose_name='質問ID',
                                 related_name='question_answer_detail', on_delete=models.PROTECT, null=False)
    question_detail = models.ForeignKey(QuestionDetail, verbose_name='質問詳細ID',
                                        related_name='question_detail_answer_detail', on_delete=models.PROTECT, null=False)
    answer = models.ForeignKey(Answer, verbose_name='回答ID',
                               related_name='answer_detail', on_delete=models.PROTECT, null=False)
    content = models.CharField(verbose_name='回答内容', max_length=200, null=False)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'AnswerDetail'
        db_table = 'answer_detail'


class MChoice(models.Model):
    """選択肢マスタモデル"""

    question = models.ForeignKey(Question, verbose_name='質問ID',
                                 related_name='question_choice', on_delete=models.PROTECT)
    question_detail = models.ForeignKey(QuestionDetail, verbose_name="質問詳細ID", 
                                        related_name='detail_choice', on_delete=models.PROTECT, null=False)
    choice_item = models.CharField(verbose_name='選択項目', max_length=200, null=False)
    delete_flag = models.PositiveIntegerField(verbose_name="削除フラグ", null=False, default=0)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'MChoice'
        db_table = 'm_choice'

        constraints = [
            models.UniqueConstraint(fields=['question', 'question_detail', 'choice_item'],
                                    name='unique_m_choice'),
        ]

    def __str__(self):
        return self.choice_item
