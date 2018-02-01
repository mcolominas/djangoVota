from django.contrib import admin

# Register your models here.
from .models import Encuesta, Opcion, Voto

class OpcionesEnLinea(admin.StackedInline):
	model = Opcion
	extra = 2

class EncuestaAdmin(admin.ModelAdmin):
	readonly_fields = ('usuario',)

	def save_model(self, request, obj, form, change):
		obj.usuario = request.user
		super().save_model(request, obj, form, change)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(usuario=request.user)
	fieldsets = (('Información basica', { 'fields' : ('nombre', 'descripcion', 'multirespuesta', ('inicio', 'fin'))}),)
	list_display = ('nombre', 'activo')
	inlines = [OpcionesEnLinea]

class OpcionAdmin(admin.ModelAdmin):
	readonly_fields = ('encuesta',)
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "encuesta":
			kwargs["queryset"] = Encuesta.objects.filter(usuario=request.user)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)

	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return qs
		return qs.filter(encuesta__usuario=request.user)
	fields = ('encuesta', 'nombre')
	list_display = ('nombre', 'encuesta', 'votos_totales', 'porcentaje_votos')
	ordering = ('-encuesta', )
	list_filter = ('encuesta',)

admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Opcion, OpcionAdmin)
admin.site.register(Voto)