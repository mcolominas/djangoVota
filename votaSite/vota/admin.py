from django.contrib import admin

# Register your models here.
from .models import Encuesta, AccesoEncuesta

admin.site.register(Encuesta)
admin.site.register(AccesoEncuesta)