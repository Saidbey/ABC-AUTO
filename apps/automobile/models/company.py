from django.db import models
from apps.shared.django.model import BaseModel


class CarCompany(BaseModel):
    title = models.CharField(max_length=100, null=True)
    logo = models.ImageField(upload_to='company_logo')
    about = models.TextField(null=True)

    def __str__(self):
        return str(self.title)
