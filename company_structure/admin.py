from django.contrib import admin
from company_structure.models import AreaModel as Area

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista del modelo
    list_display = ("name", "area_id", "email")
    # Columnas con enlaces clickeables para entrar en el detalle del registro
    list_display_links = ("name",)
    # Campos por los que se pueden buscar
    search_fields = ("area_id", "name",)
    # Filtros laterales
    list_filter = ("creation_date",)
    # Orden por defecto
    ordering = ("name",)
    # Campos de solo lectura
    readonly_fields = ("creation_date",)