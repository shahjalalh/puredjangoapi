from django.db import models
from userprofile.models import UserProfile


# Create your models here.


class BookGenre(models.Model):
    genre = models.CharField(max_length=255, blank=False, null=False, help_text="Genre of the book")


class Book(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False, help_text="Book Name")
    book_genre = models.ForeignKey(BookGenre, on_delete=models.SET_NULL, null=True, blank=True, help_text="Book Genre")
    book_owner = models.ForeignKey(UserProfile, blank=False, null=False)


