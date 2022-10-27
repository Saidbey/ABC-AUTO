from django.db import models
from ckeditor.fields import RichTextField

# project
from apps.shared.django.model import BaseModel
from apps.automobile.models import Car


class News(BaseModel):
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/news')  # I prefered not to set validator here
    video = models.FileField(upload_to='blog/news', blank=True)
    summary = models.TextField()
    content = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
