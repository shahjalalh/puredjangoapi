from django.contrib import admin
from books.models import BookGenre, Book

# Register your models here.

admin.site.register(BookGenre)
admin.site.register(Book)
