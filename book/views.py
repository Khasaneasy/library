from django.db.models import Q
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    """Viewset для управления книгами."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        book = self.get_object()
        new_status = request.data.get("status")
        if not new_status:
            return Response({'error': 'Статус не указан'}, status=400)
        if new_status in dict(Book.STATUS_CHOICES):
            book.status = new_status
            book.save()
            return Response({'status': 'success', 'new_status': new_status})
        return Response({'error': 'Неверный статус'}, status=400)

    @action(detail=False, methods=['get'])
    def search(self, request):
        """Поиск книги по title, author или year."""
        query = request.query_params.get('q', '').strip()
        if not query:
            return Response(
                {'error': 'Не указан параметр поиска'},
                status=400)

        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(year__icontains=query)
        )
        if not books.exists():
            return Response(
                {'error': 'Книги по запросу не найдены'},
                status=404)

        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
