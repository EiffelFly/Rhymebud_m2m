from django.db import models
from django.utils.translation import gettext_lazy as _
from machine.models import Machine
from application.models import Application

# Create your models here.
class Company(models.Model):
    
    hash = models.CharField(
        verbose_name=_('Hash'),
        max_length=128,
        blank=True,
    )

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
        blank=True,
    )

    company_description = models.TextField(
        verbose_name=_('Company Description'),
        max_length=262144,
        blank=True,
    )

    company_website = models.URLField(
        verbose_name=_('Company Website'),
        max_length=1024,
        blank=True,
    )

    machine = models.ManyToManyField(
        Machine,
        related_name='companys',
        verbose_name=_('Machines'),
        blank=True,
    )

    application = models.ManyToManyField(
        Application,
        related_name='companys',
        verbose_name=_('Applications'),
        blank=True,
    )
    
    #diagram = models.ImageField()

    

