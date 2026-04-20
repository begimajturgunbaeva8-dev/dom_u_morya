from django.db import models
from houses.models import House


class Order(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name="Дом")
    name = models.CharField("Имя", max_length=50)
    phone = models.CharField("Телефон", max_length=20)
    date = models.DateField("Дата", auto_now_add=True)

    def __str__(self):
        return f"Заказ от {self.name} на дом {self.house.name}"
