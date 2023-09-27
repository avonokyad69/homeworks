from django.shortcuts import render, redirect

from books.models import Book
from datetime import datetime

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)

def books_pagi(request, date):
    template = 'books/books_list.html'
    books = Book.objects.order_by('pub_date')
    date_object = datetime.strptime(date, '%Y-%m-%d').date()
    date_prev = ''
    date_next = ''
    if Book.objects.filter(pub_date__lt=date_object).values('pub_date').first() is not None:
        date_prev = Book.objects.filter(pub_date__lt=date_object).values('pub_date').first()['pub_date']
    if Book.objects.filter(pub_date__gt=date_object).values('pub_date').first() is not None:
        date_next = Book.objects.filter(pub_date__gt=date_object).values('pub_date').first()['pub_date']
    books = books.filter(pub_date=date)
    context = {
        'books': books,
        'date_prev': date_prev,
        'date_next': date_next,
    }
    return render(request, template, context)