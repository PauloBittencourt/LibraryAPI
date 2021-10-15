from rest_framework import viewsets
from books.api import serializers
from books.models import models

class BooksViewSet(viewsets.BookViewSet):
    serializers = serializers.BooksSerializer
    queryset = models.Books.objects.all()