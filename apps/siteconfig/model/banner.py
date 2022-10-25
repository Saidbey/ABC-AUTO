from django.db import models
from apps.shared.django.model import BaseModel


class Banner(BaseModel):
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True, help_text='Display this banner on the website.')

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='banners/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
