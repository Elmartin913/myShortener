from django.db import models

from .utils import (code_generator, create_shortcode)

# Create your models here.


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=None)
        return qs


class ShortURL(models.Model):
    url = models.CharField(max_length=256, )
    shortcode = models.CharField(max_length=15, unique=True, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
