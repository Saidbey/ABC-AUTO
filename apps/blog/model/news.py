from django.db import models
from apps.shared.django.model import BaseModel
from ckeditor.fields import RichTextField

# project
from apps.automobile.models import CarCompany, Car


class News(BaseModel):
    car = models.ForeignKey(Car, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='news')
    video = models.FileField(upload_to='news', blank=True)
    summary = models.TextField()
    content = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
