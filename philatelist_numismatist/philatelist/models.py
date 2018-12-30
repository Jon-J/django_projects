from django.db import models

# Create your models here.
class StampsGroup(models.Model):
    """Collections for stamps"""
    country  = models.CharField(max_length=250)
    image = models.CharField(max_length=4000)

    def __str__(self):
        return self.country

class Stamp(models.Model):
    stamp_group = models.ForeignKey(StampsGroup, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    used = models.BooleanField(default=True)
    is_fav = models.BooleanField(default=False)

    def __str__(self):
        return self.year+ " - " + self.value
