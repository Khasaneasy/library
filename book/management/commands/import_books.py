import json
from datetime import datetime
from django.core.management.base import BaseCommand

from book.models import Book


class Command(BaseCommand):
    help = 'Импорт книг из JSON'

    def handle(self, *args, **kwargs):
        try:
            with open('books.json', 'r', encoding='utf-8') as file:
                books = json.load(file)
                for book in books:
                    book['year'] = datetime.strptime(book['year'], '%Y-%m-%d').date()
                    Book.objects.create(**book)
            self.stdout.write(self.style.SUCCESS(
                'Данные импортированны.')
            )
        except FileNotFoundError:
            self.stdout.write(self.style.SUCCESS(
                'Файл books.json не найден.')
            )
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f"Ошибка при добавлении книги: {book}. Причина: {e}")
            )
