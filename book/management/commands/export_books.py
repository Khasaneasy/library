import json
from django.core.management.base import BaseCommand

from book.models import Book


class Command(BaseCommand):
    help = 'Экспорт книг в JSON'

    def handle(self, *args, **kwargs):
        books = Book.objects.values(
            'author',
            'title',
            'year',
            'status'
        )
        books_list = []
        for book in books:
            book['year'] = book['year'].strftime('%Y-%m-%d')
            books_list.append(book)

        with open("books.json", "w", encoding="utf-8") as file:
            json.dump(list(books), file, ensure_ascii=False)
        self.stdout.write(self.style.SUCCESS(
            "Данные экспортированы в books.json"))
