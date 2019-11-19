from django.db import models
from django.conf import settings

class ViberUser(models.Model):
    viber_id = models.CharField(max_length=256)
    country = models.CharField(max_length=256, null = True)
    name = models.CharField(max_length=256, null = True)
    language = models.CharField(max_length=256, null = True)
    is_active = models.BooleanField(default=True)
    is_bloked = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=256, null = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True, blank=True)

    class Meta:
        #verbose_name = 'Viber пользователь' #переводит имя JobPosition на руский в одиночном числе
        verbose_name_plural = 'Viber пользователи' #переводит JobPosition статей на руский в множественном числе
# Create your models here.
