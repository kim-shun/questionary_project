from accounts.models import CustomUser
from django.db import models


class Genre(models.Model):
    """質問ジャンルマスタモデル"""

    genre = models.CharField(verbose_name='質問ジャンル', max_length=60, null=False, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Genre'
        db_table = 'genre'

    def __str__(self):
        return self.genre


class Question(models.Model):
    """質問テーブルモデル"""

    question_id = models.PositiveIntegerField(verbose_name='質問ID', null=False)
    genre = models.ForeignKey(Genre, verbose_name="質問ジャンル",
                              related_name='question_genre_id', on_delete=models.PROTECT, null=False)
    question_order = models.PositiveIntegerField(verbose_name="質問順序", null=False)
    question_type = models.CharField(verbose_name='質問形式', max_length=20, null=False)
    content = models.TextField(verbose_name='質問内容', null=False)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Question'
        db_table = 'question'

        constraints = [
            models.UniqueConstraint(fields=['question_id', 'genre', 'question_order'],
                                    name='unique_question'),
        ]

        indexes = [
            models.Index(fields=['question_id', 'genre', 'question_order', 'question_type', 'content'],
                         name='idx_question')
        ]

    def __str__(self):
        return self.question_id
