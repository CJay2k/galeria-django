from django.db import models
from django.contrib.auth.models import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class Photo(models.Model):
    owner = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    # width = models.IntegerField(default=0)
    # height = models.IntegerField(default=0)
    # image = models.ImageField(null=True, blank=True, width_field="width", height_field="height")
    image = models.ImageField(null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp"]

    def delete(self, *args, **kwargs):
        self.image.delete()
        return super(Photo, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.owner = str(get_current_authenticated_user())
        return super(Photo, self).save(*args, **kwargs)
