from django import forms

from orders.models import Order
from houses.models import House


class OrderForm(forms.ModelForm):
    # Заявку можно оставить только на активный дом.
    house = forms.ModelChoiceField(
        queryset=House.objects.filter(active=True), widget=forms.HiddenInput()
    )
    personal_data = forms.BooleanField(
        label="Я согласен на обработку персональных данных", required=True
    )

    class Meta:
        model = Order
        fields = ["house", "name", "phone"]
