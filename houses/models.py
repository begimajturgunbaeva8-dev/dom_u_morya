from django.db import models


class House(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    photo = models.ImageField(
        "Фото", upload_to="houses/photos/", blank=True, default=""
    )
    active = models.BooleanField("Активно", default=True)


    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
        ordering = ["name"]

    def __str__(self):
        return self.name
