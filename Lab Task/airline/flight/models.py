from django.db import models

# Create your models here.


# class Airport(models.Model):
#     city = models.CharField(max_length=64)
#     code = models.CharField(max_length=3)

#     def __str__(self):
#         return f'{self.city}({self.code})'


# class Flight(models.Model):
#     origin = models.ForeignKey(
#         Airport, on_delete=models.CASCADE, related_name='departure')
#     destination = models.ForeignKey(
#         Airport, on_delete=models.CASCADE, related_name='arrival')
#     duration = models.IntegerField()

#     def __str__(self):
#         return f"{self.origin} to {self.destination}"
