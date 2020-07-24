from django.db import models

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

    #machine = models.ManyToManyField()
    #application = models.ManyToManyField()

    

