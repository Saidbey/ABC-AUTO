from django.db import models
import datetime

from apps.shared.utils.valid_size import validate_file_size, validate_img_size
from apps.shared.django.model import BaseModel
from .position_category import year


class Usedcars(BaseModel):
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE)
    year = models.PositiveIntegerField('year', choices=year(), default=datetime.datetime.now().year)
    cost = models.FloatField()
    photo = models.ImageField(blank=True, null=True, upload_to='car/usedcars', validators=[validate_img_size])
    video = models.FileField(blank=True, null=True, upload_to='car/usedcars', validators=[validate_file_size])
    engine = models.CharField(max_length=255)
    transmission_box = models.CharField(max_length=255)
    drive_type = models.CharField(max_length=255)
    mileage = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=True, default=0.0)

    class Meta:
        verbose_name_plural = 'Used Cars'

    def __str__(self):
        return f"{self.car} {self.year}"

