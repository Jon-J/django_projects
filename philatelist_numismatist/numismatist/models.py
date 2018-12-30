from django.db import models

# Create your models here.
class CoinsGroups(models.Model):
    """Collections for coins and notes"""
    country  = models.CharField(max_length=250)
    monetary_units = models.CharField(max_length=250)

    def __str__(self):
        return self.country

class Coin(models.Model):
    coins_group = models.ForeignKey(CoinsGroups, on_delete=models.CASCADE)
    type_currency = models.CharField(max_length=250)
    denomination = models.CharField(max_length=250)
    year = models.CharField(max_length=250)

    def __str__(self):
        return self.type_currency + " - " + self.denomination
