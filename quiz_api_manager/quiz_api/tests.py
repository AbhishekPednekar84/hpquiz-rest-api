import pytest

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Book, Question


@pytest.fixture
def create_book(db):
    return Book.objects.create(title="title1", description="desc")


@pytest.fixture
def create_question(db, create_book):
    return Question.objects.create(
        question="question",
        option_a="a",
        option_b="b",
        option_c="c",
        option_d="d",
        c_option="a",
        book_id=create_book
    )


@pytest.fixture
def create_user():
    return User.objects.create_user("HPQuiz", "HPQuiz@hpquiz.com", "HPQuizpassword")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def api_client_with_credentials(create_user, api_client):
    api_client.force_authenticate(user=create_user)
    yield api_client



@pytest.mark.django_db
def test_book_creation(create_book):
    assert create_book.title == "title1"


@pytest.mark.django_db
def test_get_books_list(client):
    url = reverse("book-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_question_creation(create_question):
    assert create_question.question == "question"


@pytest.mark.django_db
def test_get_questions_list(client):
    url = reverse('questions-list-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_question_detail(client):
    url = reverse("question-list")
    response = client.get(url, data={"book_id": 1})
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_book_with_authentication(api_client_with_credentials):
    data = {
        "title": "Test title",
        "description": "Test description"
    }
    url = reverse("book-list")
    response = api_client_with_credentials.post(url, data)
    assert response.status_code == 201
