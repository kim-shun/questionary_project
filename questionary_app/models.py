from accounts.models import CustomUser
from django.db import models


class Genre(models.Model):
    """質問ジャンルモデル"""

    genre = models.CharField(verbose_name='質問ジャンル', max_length=60, null=False, unique=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    
    class Meta:
        verbose_name_plural = 'Genre'
        db_table = 'genre'

    def __str__(self):
        return self.genre
