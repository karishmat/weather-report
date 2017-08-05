from django.db import models
from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Country(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='title')


class Temperature(TimeStampedModel):
    temperature = models.CharField(_('temperature'), max_length=20)
    year = models.IntegerField(_('year'))
    month = models.CharField(_('month'),max_length=10)
    season = models.CharField(_('season'),max_length=15)
    type = models.CharField(_('Type'), max_length=10, default='')
    country = models.ForeignKey(Country)
