from django.contrib import admin

# Register your models here.
from .models import Book, Author, Genre, BookInstance

# admin.site.register(Book)


admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(BookInstance)
