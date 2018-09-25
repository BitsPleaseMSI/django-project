from django.contrib import admin
from .models import Author, Book, BookInstance, Language, Genre
# Register your models here.

admin.site.register(Language)

class BookAdminInline(admin.TabularInline):
    model = Book
    extra = 1

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BookAdminInline]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back', 'borrower')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (
            None, {
                'fields':('book', 'imprint', 'id')
            }
        ),
        (
            'Availability', {
                'fields':('status', 'due_back', 'borrower')
            }
        )
    )

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'books')
