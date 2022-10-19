from django import forms


class AccumulativePercentageForm(forms.Form):
    amount = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "amount-size"})
    )
    percentage = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "percentage-size"})
    )
    period = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "period-size"})
    )
