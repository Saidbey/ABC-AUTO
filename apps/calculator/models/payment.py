# import numpy_financial as npf

from django.db import models
from apps.shared.django.model import BaseModel

# CHOOSE_PERCENT = [
#     (.019, 1.9),
#     (.05, 5),
#     (.012, 12)
# ]


# def payment(percent, month, sum):
#     total = npf.pmt(percent / 12, month, sum) * -1
#     return total


class Payment(models.Model):
    credit = models.ForeignKey('calculator.Cridet', on_delete=models.CASCADE, related_name='payments')
    order = models.IntegerField(default=1)
    sum = models.DecimalField(max_digits=15, decimal_places=3, default=0)
    percent = models.FloatField(default=12)
    per_month = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.credit)
