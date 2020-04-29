from django.shortcuts import render
from .serializers import BookSerializer, QuestionSerializer, AnalyticSerializer
from .models import Book, Question, Analytic
from rest_framework import viewsets, permissions


class BookViewSet(viewsets.ModelViewSet):

    # def get_queryset(self):
    #     book_id = self.request.query_params.get("q")
    #     print(book_id)
    #     queryset = Book.objects.all(id=book_id)
    #     return queryset

    queryset = Book.objects.order_by("id")
    serializer_class = BookSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]


class QuestionViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        book_id = self.request.query_params.get("book_id", None)
        if book_id:
            queryset = Question.objects.filter(book_id=book_id).order_by("id")
        else:
            queryset = Question.objects.all()
        return queryset

    # queryset = Question.objects.all()
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
