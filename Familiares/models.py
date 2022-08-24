from importlib.util import module_for_loader
from django.db import models

# Create your models here.
class miembros(models.Model):
    nombre = models.CharField(max_length=50)
    saldo = models.FloatField()
    fecha_nac = models.DateField()

    