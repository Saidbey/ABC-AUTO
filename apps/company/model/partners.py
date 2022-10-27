from django.db import models


class Partners(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='company/parters')
    link = models.URLField()

    class Meta:
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name
