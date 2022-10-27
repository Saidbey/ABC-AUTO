from django.db import models
from apps.shared.django.model import BaseModel
from colorfield.fields import ColorField

from apps.shared.utils.valid_size import validate_file_size, validate_img_size
from apps.users.models import User
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
    model = models.CharField(max_length=255)
    cost_from = models.DecimalField(max_digits=9, decimal_places=3, null=True)
    color = ColorField(choices=COLOR_CHOICES)
    carbody = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True)
    description = models.TextField()
    internal_possibility = models.TextField()
    appearance = models.TextField()
    internal_photo = models.ImageField(upload_to='car/indernal_pics', validators=[validate_img_size])
    external_photo = models.ImageField(upload_to='car/external_pics', validators=[validate_img_size])
    side_photo = models.ImageField(upload_to='car/side_pics', validators=[validate_img_size])
    video = models.FileField(blank=True, null=True, upload_to='car/video', validators=[validate_file_size])
    bonusForCustomers = models.ManyToManyField(Gifts, related_name='gifts')
    discount = models.PositiveIntegerField(null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.model)


class CarLikes(models.Model):
    likeusers = models.ManyToManyField(User)
    likepost = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, related_name='likepost')




