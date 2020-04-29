import random
from .serializers import BookSerializer, QuestionSerializer, AnalyticSerializer
from .models import Book, Question, Analytic
from rest_framework import viewsets, permissions


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.order_by("id")
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class QuestionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        filters = ["id", "-id", "question", "-question", "option_a", "-option_a",
                   "option_b", "-option_b", "option_c", "-option_c", "option_d", "-option_d"]

        book_id = self.request.query_params.get("book_id", None)
        if book_id:
            queryset = Question.objects.filter(book_id=book_id).order_by(random.choice(filters))[:25]
        else:
            queryset = Question.objects.all()
        return queryset

    serializer_class = QuestionSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class AnalyticViewSet(viewsets.ModelViewSet):
    queryset = Analytic.objects.order_by("-id")
    serializer_class = AnalyticSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]
