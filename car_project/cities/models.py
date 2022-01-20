from django.db import models
from cars.models import Cars
from parties.models import Parties
# Create your models here.


class Cities(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Name')
    code = models.CharField(max_length=255, blank=True, null=True, verbose_name='Code')
    city_file = models.FileField(upload_to='uploads/cities/')
    
    def __str__(self):
        return self.name


class CityCars(models.Model):
    city = models.ForeignKey(to=Cities, on_delete=models.CASCADE, related_name='city_car')
    car = models.ForeignKey(to=Cars, on_delete=models.CASCADE, related_name='city_car')
    operator = models.ForeignKey(to=Parties, on_delete=models.CASCADE, limit_choices_to={'user_type': '2'}, related_name='city_car')
    
    @property
    def operator_code(self):
        if self.operator:
            return self.operator.code
