from django import forms
from orders.models import Order
from houses.models import House


class OrderForm(forms.ModelForm):
    house = forms.ModelChoiceField(
        queryset=House.objects.all(), widget=forms.HiddenInput()
    )
    personal_data_consent = forms.BooleanField(
        required=True, label="Я согласен на обработку персональных данных"
    )

    class Meta:
        model = Order
        fields = ["house", "name", "phone"]
