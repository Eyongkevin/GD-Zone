from django import forms


class AccumulativePercentageForm(forms.Form):
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "amount-size"}), label="B"
    )
    percentage = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "percentage-size"}), label=" %"
    )
    period = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "period-size"}), label=" P"
    )
