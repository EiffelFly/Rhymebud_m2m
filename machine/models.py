from django.db import models
from django.utils.translation import gettext_lazy as _
from unidecode import unidecode
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save

# Create your models here.
class Machine(models.Model):

    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
        blank=True,
    )

    description = models.TextField(
        verbose_name=_('Machine Description'),
        max_length=262144,
        blank=True,
    )

    slug = models.SlugField(
        unique=True, 
        null=True, 
        blank=True, 
        max_length=255
    )

    def __str__(self):
        return self.name
    
    #diagram = models.ImageField()

def create_slug(instance, new_slug=None):
    '''
        Recursive function to check whether slug and instance has been created
        
    '''
    slug = slugify(unidecode(instance.name))
    if new_slug is not None:
        slug = new_slug
    querySet = Machine.objects.filter(slug=slug).order_by("-id")
    exists = querySet.exists()
    if exists:
        new_slug = f"{slug}-{querySet.first().id}"
        return create_slug(instance, new_slug=new_slug)
    return slug

@receiver(pre_save, sender=Machine)
def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)