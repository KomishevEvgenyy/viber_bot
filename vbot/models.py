from django.db import models
from django.conf import settings

class ViberUser(models.Model):
    viber_id = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    language = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)
    is_bloked = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=256)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, blank=True)
# Create your models here.
