from django import forms


class HouseFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, label="от")
    max_price = forms.IntegerField(required=False, label="до")
    query = forms.CharField(required=False, label="описание")
