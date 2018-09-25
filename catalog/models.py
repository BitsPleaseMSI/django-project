import uuid
from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre')

    def books(self):
        return Book.objects.filter(genre=self.id).count()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(default='Summary of by' , max_length=1000, help_text='Describe the book in brief')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 digit ISBN number')
    genre = models.ManyToManyField(Genre, help_text='Select genre for this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())
    display_genre.short_discription = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

class BookInstance(models.Model):
    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,
        unique=True,
        help_text='Unique ID for this Particular book'
    )
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(default='imp1', max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintainance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices = LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (
            ('can_mark_returned', 'Set book as returned'),
        )

    def __str__(self):
        return self.book.title + ' ' + str(self.id)

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Language(models.Model):
    lang = models.CharField(max_length=200, help_text='Enter book\'s natural language')

    def __str__(self):
        return self.lang
