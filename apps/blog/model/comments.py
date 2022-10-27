from django.db import models
from embed_video.fields import EmbedVideoField

# project
from apps.shared.utils.valid_size import validate_img_size
from apps.shared.django.model import BaseModel
from apps.automobile.models import Car


class Comment(BaseModel):
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name='comments', blank=True)
    author = models.CharField(max_length=200)
    text = models.TextField()
    pic = models.ImageField(upload_to='blog/comment', null=True, blank=True, validators=[validate_img_size])
    videoUrl = EmbedVideoField(null=True, blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return 'Comment {}... by {}'.format(self.text[:10], self.author)
    