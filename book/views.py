from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


User = get_user_model()


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['post'])
    def change_status(self, request, pk=None):
        book = self.get_object()
        new_status = request.data.get("status")
        if new_status in dict(Book.STATUS_CHOICES):
            book.status = new_status
            book.save()
            return Response({'status': 'success', 'new_status': new_status})
        return Response({'error': 'Неверный статус'}, status=400)
