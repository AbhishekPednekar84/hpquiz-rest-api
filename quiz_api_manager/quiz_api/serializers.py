from rest_framework import serializers
from .models import Book, Question, Analytic


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnalyticSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytic
        fields = "__all__"

