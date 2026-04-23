from django.db import models


class Review(models.Model):
    author = models.CharField("Имя автора", max_length=100)
    text = models.TextField("Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Отзыв от {self.author}"
