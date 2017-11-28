from django.db import models

from cutter.models import ShortURL

# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, shortinstance):
        if isinstance(shortinstance, ShortURL):
            obj, created = self.get_or_create(short_url=shortinstance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    short_url = models.OneToOneField(ShortURL)
    count = models.IntegerField(default=0)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{}'.format(self.count)
