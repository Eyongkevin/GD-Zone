from django.urls import path
from . import views

app_name = "user"
urlpatterns = [path("login/", views.UserLogin.as_view(), name="login")]
