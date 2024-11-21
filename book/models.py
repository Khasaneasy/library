from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

BOOK_LENGTH = 200
STATUS_LENGTH = 25


class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'В наличии'),
        ('issued', 'Выдана')
    ]

    title = models.CharField(
        max_length=BOOK_LENGTH
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='books',
        verbose_name='Автор'
    )
    year = models.DateField()
    status = models.CharField(
        max_length=STATUS_LENGTH,
        choices=STATUS_CHOICES,
        default='available',
    )

    def __str__(self):
        return self.title

# Надо добавить : вьюшку добить админку менеджеры ввод вывод 