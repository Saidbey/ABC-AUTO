from django.contrib.auth.models import GroupManager
from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import Group


class Role(models.Model):
    name = models.JSONField(default=dict, null=True, blank=True) # {"uz":"Shifokor","en":"Doctor"}
    groups = models.ManyToManyField(Group, related_name='roles')

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)


class UserRole(models.Model):
    user = models.ForeignKey('users.User', CASCADE)
    role = models.ForeignKey('users.Role', CASCADE)

    is_active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)
