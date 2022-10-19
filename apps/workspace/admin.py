from django.contrib import admin
from .models import Statistic

# Register your models here.
@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ["number_of_clicks"]
