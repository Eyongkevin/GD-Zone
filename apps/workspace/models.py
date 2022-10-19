from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import F

# Create your models here.
class Statistic(models.Model):
    number_of_clicks = models.IntegerField(_("Number Of Clicks"))

    @classmethod
    def clicks_count(cls) -> int:
        """get the number of clicks

        Returns:
            integer: Number of clicks
        """
        return cls._default_manager.all().first().number_of_clicks

    @classmethod
    def increment_or_create(cls) -> None:
        """Create or update the number of clicks by incrementing"""

        if cls._default_manager.exists():
            cls._default_manager.filter(number_of_clicks__gt=0).update(
                number_of_clicks=F("number_of_clicks") + 1
            )
        else:
            statistic = cls._default_manager.create(number_of_clicks=1)
            statistic.save()
