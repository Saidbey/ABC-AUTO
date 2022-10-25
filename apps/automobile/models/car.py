from django.db import models
from apps.shared.django.model import BaseModel
from colorfield.fields import ColorField
from .company import CarCompany
from .gifts import Gifts


class Car(BaseModel):
    COLOR_CHOICES = [
        ("#FFFFFF", "white"),
        ("#000000", "black"),
        ("#FF0000", "red")
    ]

    TYPE_CHOICES = [
        ("Oilaviy", "Family"),
        ("Sports", "Sports"),
        ("Sayohat", "Journey")
    ]

    company = models.ForeignKey(CarCompany, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    cost_from = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    color = ColorField(choices=COLOR_CHOICES)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True)
    internal_possibility = models.TextField()
    appearance = models.TextField()
    internal_photo = models.ImageField(upload_to='indernal_pics')
    external_photo = models.ImageField(upload_to='external_pics')
    side_photo = models.ImageField(upload_to='side_pics')
    bonusForCustomers = models.ManyToManyField(Gifts, related_name='gifts')
    discount = models.IntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)




