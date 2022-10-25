from django.db import models

from apps.shared.django.queryset import DeleteManager


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeleteModel(models.Model):
    is_delete = models.BooleanField(default=False)

    objects = DeleteManager()

    class Meta:
        abstract = True

    def delete(self, **kwargs):
        self.is_delete = True
        self.save()
