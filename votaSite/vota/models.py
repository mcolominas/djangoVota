from django.conf import settings
from django.db import models

# Create your models here.
class Encuesta(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	multirespuesta = models.BooleanField()
	descripcion = models.CharField(max_length=200)
	inicio = models.DateTimeField('Data de publicacion')
	fin = models.DateTimeField('Data de cerrar')

class OpcionesEncuestas(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)

class VotosEncuestas(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	opcion = models.ForeignKey(OpcionesEncuestas, on_delete=models.CASCADE)

class AccesoEncuesta(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
