from django.db import models
from django.contrib.auth.models import User

PARTY_TYPE = (
    ('1', 'Manager'),
    ('2', 'Operator'),
)


class Parties(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=6, null=True)
    user_type = models.CharField(max_length=1, choices=PARTY_TYPE, null=False)
    user = models.OneToOneField(User, related_name='party', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.full_name

    @property
    def is_manager(self):
        return self.user_type == '1'

    @property
    def is_operator(self):
        return self.user_type == '2'
