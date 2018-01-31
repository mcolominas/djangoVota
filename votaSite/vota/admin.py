from django.contrib import admin

# Register your models here.
from .models import Encuesta, Opcion, Voto

class OpcionesEnLinea(admin.StackedInline):
	model = Opcion
	extra = 2

class EncuestaAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(usuario=request.user)

	list_display = ('nombre', 'activo')
	inlines = [OpcionesEnLinea]

class OpcionAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(encuesta__usuario=request.user)

	list_display = ('nombre', 'encuesta', 'votos_Totales')
	ordering = ['-encuesta']

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Opcion, OpcionAdmin)
admin.site.register(Voto)