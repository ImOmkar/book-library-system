from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm
from .scraping import scrape_books
from .constants import CATEGORIES
from django.contrib.auth.decorators import login_required
from .decorators import admin_required, superadmin_required
from django.contrib import messages

def home(request):
    return render(request, "books/home.html")

def book_list(request):
    books = Book.objects.all().order_by('-created_at')
    search = request.GET.get("search")
    genre = request.GET.get("genre")
    if search:
        books = books.filter(title__icontains=search)
    if genre:
        books = books.filter(genre=genre)
    return render(request, "books/book_list.html", {
        "books": books,
        "categories": Book.objects.values_list("genre", flat=True).distinct()
    })

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

@login_required
@admin_required
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book added successfully!")
            return redirect("book_list")
        else:
            messages.error(request, "Failed to add a book")
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {"form": form})

@login_required
@admin_required
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully!")
            return redirect("book_list")
        else:
            messages.error(request, "Failed to update a book")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})

@login_required
@superadmin_required
def delete_book(request, pk):
    try:
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        messages.success(request, "Book deleted successfully!")
    except Exception as e:
        messages.error(request, "Failed to delete a book")
    return redirect("book_list")    

@login_required
@admin_required
def scrape_books_view(request):
    if request.method == "POST":
        category = request.POST.get("category")
        slug = CATEGORIES.get(category)
        # try:
        books = scrape_books(slug)
        for book in books:
            Book.objects.create(
                title=book["title"],
                genre=category,
                price=book["price"],
                description=book["description"],
                image_url=book["image_url"]
            )
        messages.success(request, f"{len(books)} books scraped successfully!")
        # except Exception as e:
            # messages.error(request, f"Failed to scrap books for a {category} category")
        return redirect("book_list")
    return render(request, "books/scrape.html", {"categories": CATEGORIES.keys()})

