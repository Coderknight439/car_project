from django.db import models

# Create your models here.


class Cars(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='Code')
    
    def __str__(self):
        return self.name

