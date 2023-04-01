from django.db import models

class Juguete(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
