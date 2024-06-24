from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, max_length=15000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    is_primary = models.BooleanField(default=True)
    prep_time_span = models.IntegerField(default=0)  # Prep minutes including deadtime like like brining.
    prep_time_human = models.IntegerField(default=0)  # Prep minutes no deadtime.
    cook_time_span = models.IntegerField(default=0)  # time to cook including deadtime in the oven.
    cook_time_human = models.IntegerField(default=0)  # time spent cooking directly
