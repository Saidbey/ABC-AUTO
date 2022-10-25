from django.db import models
from django.db.models import Min
import datetime

# Project
from apps.automobile.models.car import Car
from apps.shared.django.model import BaseModel


def year():
    year_dropdown = []
    for y in range(2011, (datetime.datetime.now().year + 3)):
        year_dropdown.append((y, y))
    return year_dropdown


class PositionCategory(BaseModel):
    # relations
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE)
    # fields
    name = models.CharField(max_length=255, null=True)
    year = models.IntegerField('year', choices=year(), default=datetime.datetime.now().year)
    cost = models.FloatField()
    engine = models.CharField(max_length=255)
    engine_size = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    available_volume = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    transmission_box = models.CharField(max_length=255)
    overclocking_time = models.FloatField()
    max_speed = models.IntegerField()
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, default=0.0)

    # security
    lockingRearWheelDifferential = models.BooleanField(default=False)
    automaticAutoHold = models.BooleanField(default=False)
    childSeatLock = models.BooleanField(default=False)
    front_breakes = models.CharField(max_length=100, null=True)
    rear_breakes = models.CharField(max_length=100, null=True)
    front_wheels = models.SlugField(max_length=100, null=True)
    rear_wheels = models.SlugField(max_length=100, null=True)

    # exterior
    led_headlight = models.CharField(max_length=255)
    full_weight = models.FloatField()
    empty_weight = models.FloatField()
    height = models.FloatField()
    width = models.FloatField()
    length = models.FloatField()
    seats_count = models.IntegerField()
    rearSuspension = models.CharField(max_length=100, null=True)
    brakeAssistSystem = models.CharField(max_length=100, null=True)
    antilockBrakingSystem = models.CharField(max_length=100, null=True)
    hillsStartAssist = models.CharField(max_length=100, null=True)

    # interior
    PassengerAirbagWithDeactivationFunction = models.BooleanField(default=False)
    FrontPassengerAirbag = models.BooleanField(default=False)
    AdditionalBrakeLight = models.BooleanField(default=False)
    eraGlonass = models.BooleanField(default=False)
    isofixMount = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.cost and self.car:
            min_cost = PositionCategory.objects.aggregate(Min('cost'))['cost__min']
            if min_cost is None:
                min_cost = 0
            if self.cost < min_cost:
                min_cost = self.cost
            car = Car.objects.get(id=self.car.id)
            car.cost_from = min_cost
            car.save()
        super().save(force_insert, force_update, using, update_fields)
