from django.test import TestCase, Client
from django.urls import reverse
from .models import Book

from unittest.mock import patch, Mock
from .scraping import scrape_books

class BookTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.book = Book.objects.create(
            title="Test Book",
            genre="Travel",
            price=20
        )

    def test_create_book(self):

        book = Book.objects.create(
            title="Another Book",
            genre="Art",
            price=15
        )

        self.assertEqual(book.title, "Another Book")

    def test_book_str(self):

        self.assertEqual(str(self.book), "Test Book")

    def test_book_list_view(self):

        response = self.client.get(reverse("book_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")

    def test_book_detail_view(self):

        response = self.client.get(reverse("book_detail", args=[self.book.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Book")

    def test_book_update(self):

        self.book.title = "Updated Title"
        self.book.save()

        self.assertEqual(Book.objects.get(id=self.book.id).title, "Updated Title")
        
        
        
    @patch("books.scraping.requests.get")
    def test_scrape_books(self, mock_get):

        html = """
        <html>
            <article class="product_pod">
                <h3>
                    <a title="Test Scraped Book" href="catalogue/test-book/index.html"></a>
                </h3>
                <p class="price_color">£20.00</p>
            </article>
        </html>
        """

        mock_response = Mock()
        mock_response.text = html
        mock_get.return_value = mock_response

        books = scrape_books("travel")

        self.assertIsInstance(books, list)