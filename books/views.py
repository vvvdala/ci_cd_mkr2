from django.shortcuts import render
from .models import Book

# Create your views here.
def main(request):
    latest_books = Book.objects.order_by('-id')[:5]
    return render(request, 'main.html', {'books': latest_books})