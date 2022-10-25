from django.db import models
from apps.users.models.user import phone_regex


class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=18, validators=[phone_regex], blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Address'

    def __str__(self):
        return str(self.province)

