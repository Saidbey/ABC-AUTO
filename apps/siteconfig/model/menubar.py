from django.db import models


class MenuBar(models.Model):
    title = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']