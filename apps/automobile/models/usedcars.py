from django.db import models
import datetime
from apps.shared.django.model import BaseModel
from .position_category import year


class Usedcars(BaseModel):
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE)
    year = models.IntegerField('year', choices=year(), default=datetime.datetime.now().year)
    cost = models.FloatField()
    engine = models.CharField(max_length=255)
    transmission_box = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, default=0.0)

    class Meta:
        verbose_name_plural = 'Used Cars'

    def __str__(self):
        return f"{self.car} {self.year}"

