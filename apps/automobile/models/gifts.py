from django.db import models
from apps.shared.django.model import BaseModel


class Gifts(BaseModel):
    bonus = models.CharField(max_length=100, null=True)
    details = models.TextField()

    class Meta:
        verbose_name_plural = "Bonus"

    def __str__(self):
        return str(self.bonus)
