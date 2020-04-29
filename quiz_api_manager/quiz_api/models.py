from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.title}"

    def __repr__(self):
        return f"Book({self.title})"


class Question(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    question = models.CharField(max_length=500)
    option_a = models.CharField(max_length=500)
    option_b = models.CharField(max_length=500)
    option_c = models.CharField(max_length=500)
    option_d = models.CharField(max_length=500)
    c_option = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.question}"

    def __repr__(self):
        return f"Question({self.book_id}, " \
               f"{self.question}, " \
               f"{self.option_a}, " \
               f"{self.option_b}," \
               f" {self.option_c}, " \
               f"{self.option_d}," \
               f"{self.c_option})"


class Analytic(models.Model):
    ip_address = models.GenericIPAddressField(default=None)
    city = models.CharField(max_length=50, default=None)
    country = models.CharField(max_length=50, default=None)
    date_visited = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural: "Analytics"

    def __str__(self):
        return f"{self.city} - {self.date_visited}"

    def __repr__(self):
        return f"Analytics({self.ip_address}, {self.city}, {self.country}, {self.date_visited})"

