from django.test import TestCase
import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Book


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




