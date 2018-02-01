from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Encuesta(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	multirespuesta = models.BooleanField()
	descripcion = models.CharField(max_length=200, blank=True, null=True)
	inicio = models.DateTimeField('Data de publicacion')
	fin = models.DateTimeField('Data de expiracion')

	def activo(self):
		return self.inicio <= timezone.now() and self.fin >= timezone.now()
	activo.boolean = True

	def __str__(self):
		return self.nombre

class Opcion(models.Model):
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=100)
	def votos_totales(self):
		return Voto.objects.filter(opcion=self).count()

	def porcentaje_votos(self):
		cantVotos = self.votos_totales();
		if cantVotos == 0:
			return "0%";
		else:
			return str(round((cantVotos / Voto.objects.filter(opcion__encuesta=self.encuesta).count() * 100), 2)) + "%"
	def __str__(self):
		return self.nombre

class Voto(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	opcion = models.ForeignKey(Opcion, on_delete=models.CASCADE)

class Acceso(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
