from django.db import models

# Create your models here.


class Airport(models.Model):

    origin = models.CharField(max_length=64)
    code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.origin} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, related_name='departure', on_delete=models.CASCADE)
    destination = models.ForeignKey(
        Airport, related_name='arrival', on_delete=models.CASCADE)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination}"
