from django.db import models


class Review(models.Model):
    author = models.CharField("Имя", max_length=100)
    text = models.TextField("Ваш отзыв")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name = "Отзывы"
        ordering = ["-created_at"]

    def __str__(self):
        return f"Отзыв от {self.author}"
