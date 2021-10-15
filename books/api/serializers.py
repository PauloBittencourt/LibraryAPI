from rest_framework import serializers
from books import models

class BooksSerializer(serializers.Serializer):
    class Meta:
        model = models.Books
        fields = '__all__'