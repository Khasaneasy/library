# Система управления библиотекой

## Описание проекта:
Приложение позволяет(Django Rest Framework (DRF)):
1. Добавлять книги.
2. Удалять книги по их `id`.
3. Искать книги по `title`, `author` или `year`.
4. Отображать все книги в библиотеке.
5. Изменять статус книги (например, с "в наличии" на "выдана").

Каждая книга содержит:
- `id` — уникальный идентификатор (генерируется автоматически).
- `title` — название книги.
- `author` — автор книги.
- `year` — год издания.
- `status` — статус книги ("в наличии" или "выдана").


## Импорт и экспорт данных JSON в БД:
```
python manage.py import_books.py
python manage.py export_books.py
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Khasaneasy/library
```

```
cd library
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```


Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Создать Выполнить миграции:

```
python manage.py makemigrations
python manage.py makemigrations book
```
```
python manage.py migrate
python manage.py migrate book
```

Запустить проект:

```
python manage.py runserver
```


Используемые библиотеки:
Django==3.2.16
djangorestframework==3.12.4

Автор:

>https://github.com/Khasaneasy