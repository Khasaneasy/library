from django.contrib import admin

from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'year',
        'status'
    )
    list_filter = (
        'author',
        'year',
        'status'
    )
    search_fields = (
        'title',
        'author__username'
    )
