from django.test import TestCase
import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Book, Category
from django.db.models import Count


@pytest.mark.django_db
def test_main_view_books(client):
    cover_image = SimpleUploadedFile("cover_image.jpg", b"file_content", content_type="image/jpeg")

    Book.objects.create(
        title='Тестова книга',
        description='Опис',
        publication_date='2024-05-31',
        price=10.99,
        cover_image=cover_image
    )

    response = client.get(reverse('main'))
    assert response.context['books'].count() == 1


@pytest.mark.django_db
def test_category_list_view(client):
    category1 = Category.objects.create(name='Category 1')
    category2 = Category.objects.create(name='Category 2')

    book1 = Book.objects.create(title='Book 1', description='Description 1', publication_date='2024-05-31', price=10.99)
    book2 = Book.objects.create(title='Book 2', description='Description 2', publication_date='2024-05-31', price=10.99)

    book1.categories.add(category1)
    book2.categories.add(category1, category2)

    response = client.get(reverse('category_list'))

    assert response.status_code == 200

    assert 'categories' in response.context

    annotated_categories = response.context['categories']
    assert annotated_categories.count() == 2
    assert annotated_categories[0].book_count == 2
    assert annotated_categories[1].book_count == 1

