from django.shortcuts import render
from bookapp.models import Book
from django.http import JsonResponse
# Create your views here.

def book_detail(request, id) :
    book = Book.objects.get(id=id)
    data = {
        'title' : book.title,
        'author' : book.author,
        'isbn' : book.isbn
    }
    return JsonResponse(data)

def book_list(request) :
    book = Book.objects.all()
    print(book.values())
    data = {
        'book' : list(book.values())
    }
    return JsonResponse(data)