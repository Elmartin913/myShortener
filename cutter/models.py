from django.db import models
from django.conf import settings
#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

from .utils import (code_generator, create_shortcode)
from.validators import validate_url, validate_dot_com

# Create your models here.

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)


class ShortURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ShortURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs

    def refresh_shortcode(self, items=None):
        # print(items)
        qs = ShortURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]  # last x items
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_code += 1
        return 'New code made refresh: {}'.format(new_code)


class ShortURL(models.Model):
    url = models.CharField(max_length=256, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    # short_url

    objects = ShortURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        if not 'http' in self.url:
            self.ulr = 'http://' + self.url
        super(ShortURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse('scode', kwargs={'shortcode': self.shortcode}, host='www', scheme='http', port='8000')
        return url_path
