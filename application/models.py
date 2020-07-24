from django.db import models
from django.utils.translation import gettext_lazy as _
from machine.models import Machine


# Create your models here.
class Application(models.Model):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
        blank=True,
    )

    description = models.TextField(
        verbose_name=_('Application Description'),
        max_length=262144,
        blank=True,
    )

    machine = models.ManyToManyField(
        Machine,
        related_name='applications',
        verbose_name=_('Applications'),
        blank=True,
    )

    #diagram = models.ImageField()