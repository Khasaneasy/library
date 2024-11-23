from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

app_name = 'book'

router = DefaultRouter()
router.register('books', BookViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', BookViewSet.as_view(
        {'get': 'search'}), name='book-search'),
]
