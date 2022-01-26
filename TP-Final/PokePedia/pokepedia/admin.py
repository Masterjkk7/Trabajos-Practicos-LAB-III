from django.contrib import admin
from .models import Tipo, Pokemon, Batalla

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'habilidad', 'get_tipos', 'get_apariencia')

    fieldsets = (
        (None, {
            "fields": ('nombre', 'numero', 'habilidad', 'tipo', ('apariencia', 'get_apariencia')
                
            ),
        }),
    )  

    filter_horizontal = ('tipo',)
    readonly_fields = ('get_apariencia',)

    def get_tipos(self, obj):
        return " - ".join([n.nombre for n in obj.tipo.all()])

    get_tipos.short_description = "Tipo"
    

class BatallaAdmin(admin.ModelAdmin):
    filter_horizontal = ('luchadores',)

# Register your models here.

admin.site.register(Tipo,)
admin.site.register(Pokemon, PokemonAdmin,)
admin.site.register(Batalla, BatallaAdmin,)
