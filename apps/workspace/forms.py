from django import forms


class AccumulativePercentageForm(forms.Form):
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "amount-size"}), label="B", min_value=1
    )
    percentage = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "percentage-size"}),
        label=" %",
        min_value=1,
    )
    period = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "period-size"}),
        label=" P",
        min_value=1,
    )
