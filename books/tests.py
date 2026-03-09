from django.test import TestCase
from .models import Book


class BookTests(TestCase):
    
    def test_create_book(self):
        
        book = Book.objects.create(
            title="Test Book",
            genre="Travel",
            price=20
        )
        
        self.assertEqual(book.title, "Test Book")
        
    def test_book_str(self):

        book = Book.objects.create(
            title="Another Book",
            genre="Art",
            price=15
        )

        self.assertEqual(str(book), "Another Book")