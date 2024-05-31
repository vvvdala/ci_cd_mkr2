from django.shortcuts import render
from django.db.models import Count
from .models import Book, Category

# Create your views here.
def main(request):
    latest_books = Book.objects.order_by('-id')[:5]
    return render(request, 'main.html', {'books': latest_books})

def category_list(request):
    categories = Category.objects.annotate(book_count=Count('books'))
    return render(request, 'category_list.html', {'categories': categories})