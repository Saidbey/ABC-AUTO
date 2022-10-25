from django.db import models
from apps.shared.django.model import BaseModel


class Cridet(BaseModel):
    CREDIT = 1
    LEASING = 2

    CHOICE = (
        (CREDIT, 'Credit'),
        (LEASING, 'Leasing'),
    )

    # Relations
    car = models.ForeignKey('automobile.Car', on_delete=models.CASCADE, related_name='cridets')
    model = models.ForeignKey('automobile.PositionCategory', on_delete=models.CASCADE, related_name='cridets')

    # Fields
    month = models.IntegerField(default=12)
    status = models.IntegerField(choices=CHOICE)

    def __str__(self):
        return str(self.model)

    @property
    def model_title(self):
        return self.model.title
