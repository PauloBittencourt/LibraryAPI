from django.db import models
from uuid4 import uuid4

# Create your models here.


class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    release_year = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
