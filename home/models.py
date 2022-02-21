from django.db import models


class Pumps(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)
    consumption = models.DecimalField(max_digits=9, decimal_places=2)


class Lights(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)
    consumption = models.DecimalField(max_digits=9, decimal_places=2)


class FlowMeter(models.Model):
    hours_used = models.DecimalField(max_digits=5, decimal_places=2)
    daily_cost = models.DecimalField(max_digits=9, decimal_places=2)
    consumption = models.DecimalField(max_digits=9, decimal_places=2)





















