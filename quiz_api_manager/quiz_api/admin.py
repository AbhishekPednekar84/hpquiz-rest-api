from django.contrib import admin
from .models import Book, Question, Analytic

admin.site.register(Book)
admin.site.register(Question)
admin.site.register(Analytic)
