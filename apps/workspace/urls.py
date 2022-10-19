from django.urls import path
from . import views

app_name = "workspace"

urlpatterns = [
    path(
        "accu-percentage/",
        views.accumulative_percentage_view,
        name="accumulative_percentage",
    )
]
