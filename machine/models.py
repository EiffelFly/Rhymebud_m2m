from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Machine(models.Model):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
        blank=True,
    )

    description = models.TextField(
        verbose_name=_('Company Description'),
        max_length=262144,
        blank=True,
    )

    slug = models.SlugField(
        unique=True, 
        null=True, 
        blank=True, 
        max_length=255
    )
    
    #diagram = models.ImageField()