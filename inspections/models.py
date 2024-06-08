from django.db import models


class VehicleInspection(models.Model):
    model_year = models.CharField(max_length=4)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rejection_percentage = models.CharField(max_length=10)
    reason_1 = models.CharField(max_length=255, blank=True, null=True)
    reason_2 = models.CharField(max_length=255, blank=True, null=True)
    reason_3 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.model_year} {self.make} {self.model}"
