from django.db import models

from .address import Address
from apps.users.models.user import phone_regex
from apps.shared.utils.valid_size import validate_file_size, validate_img_size


class AboutCompany(models.Model):
    title = models.CharField(max_length=100)
    about = models.TextField()
    video = models.FileField(blank=True, null=True, upload_to='company/AboutUs', validators=[validate_file_size])
    photo = models.ImageField(blank=True, upload_to='company/AboutUs', null=True, validators=[validate_img_size])
    employees = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    start_time = models.TimeField(default='10:00')
    end_time = models.TimeField(default='18:00')

    class Meta:
        verbose_name_plural = 'About Us'

    def __str__(self):
        return str(self.title)


class Filials(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True, null=True, upload_to='filials', validators=[validate_img_size])
    video = models.FileField(blank=True, null=True, upload_to='filials', validators=[validate_file_size])
    phone_number = models.CharField(max_length=18, validators=[phone_regex], blank=True, null=True, default=None)

    class Meta:
        verbose_name_plural = 'Our Filials'

    def __str__(self):
        return self.name



