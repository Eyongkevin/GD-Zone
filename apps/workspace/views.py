from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import forms
from .utils import accumulative_percentage
from .models import Statistic
from django.db.models import F
from django.http import HttpRequest

# Create your views here.


# @login_required
def accumulative_percentage_view(request: HttpRequest):
    """treat or return the form

    We treat the form by first checking if its valid, then we
    calculated the accumulative percentage for the number of periods

    Args:
        request (HttpRequest):

    Returns:
        _type_: HttpResponse
    """
    if request.method == "POST":
        form = forms.AccumulativePercentageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data["result"] = accumulative_percentage(
                data["amount"], data["percentage"], data["period"]
            )
            Statistic.increment_or_create()
    else:
        form = forms.AccumulativePercentageForm()
        data = {}
    return render(
        request, "workspace/compound_interest.html", {"form": form, "data": data}
    )
