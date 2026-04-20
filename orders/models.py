from django.db import models
from houses.models import House


class Order(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, verbose_name="Дом")
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    date = models.DateField("дата",auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
        return f"Заказ от {self.name} на дом {self.house.name}"
