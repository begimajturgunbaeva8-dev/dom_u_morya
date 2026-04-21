from django import forms


class HouseFilterForm(forms.Form):
    min_price = forms.IntegerField(required=False, label="от")
    max_price = forms.IntegerField(required=False, label="до")
    query = forms.CharField(required=False, label="описание")
    ordering = forms.ChoiceField(required=False, label="Сортировка",  choices=[("name", "По алфавиту"),
                                                                                ("price", "Дешевые сначала"),
                                                                                ("-price", "Дорогие сначала")
                                                                            ])