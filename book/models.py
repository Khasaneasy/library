from django.db import models


BOOK_LENGTH = 200
STATUS_LENGTH = 25
AUTHOR_LENGTH = 25


class Book(models.Model):
    """Модель книги в библиотеке."""
    STATUS_CHOICES = [
        ('available', 'В наличии'),
        ('issued', 'Выдана')
    ]

    title = models.CharField(
        max_length=BOOK_LENGTH
    )
    author = models.CharField(
        max_length=AUTHOR_LENGTH
    )
    year = models.DateField()
    status = models.CharField(
        max_length=STATUS_LENGTH,
        choices=STATUS_CHOICES,
        default='available',
    )

    def __str__(self):
        return self.title
