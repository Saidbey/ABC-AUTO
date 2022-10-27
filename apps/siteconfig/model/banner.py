from django.db import models
from apps.shared.django.model import BaseModel
from apps.shared.utils.valid_size import validate_img_size


class Banner(BaseModel):
    active = models.BooleanField(default=True, help_text='Display this banner on the website.')

    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='siteconfig/banners/', validators=[validate_img_size])
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
