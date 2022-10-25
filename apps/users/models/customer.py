from django.db import models

from apps.shared.django.model import BaseModel
from apps.users.models.user import phone_regex


class Customer(BaseModel):
    fullname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=18, validators=[phone_regex], blank=True, null=True, default=None)

    def __str__(self):
        return self.fullname
