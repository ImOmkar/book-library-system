from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name="book_list"),
    path('books/add/', views.add_book, name="add_book"),
    path("books/<int:pk>/", views.book_detail, name="book_detail"),
    path('books/edit/<int:pk>/', views.edit_book, name="edit_book"),
    path('books/delete/<int:pk>/', views.delete_book, name="delete_book"),
    
    path("books/scrape/", views.scrape_books_view, name="scrape_books"),
    
]
