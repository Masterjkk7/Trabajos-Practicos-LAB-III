from django.contrib import admin
from .models import Tipo, Pokemon, Lugar, Batalla
from  django.contrib.auth.models  import  Group

admin.site.unregister(Group)

class TipoAdmin(admin.ModelAdmin):
    list_filter = ['nombre']
    search_fields = ['nombre']

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'habilidad', 'get_tipos', 'get_apariencia')
    list_filter = ('nombre', 'numero', 'tipo')
    search_fields = ['nombre', 'numero', 'tipo__nombre']
    filter_horizontal = ('tipo',)
    readonly_fields = ('get_apariencia',)

    fieldsets = (
        (None, {
            "fields": ('nombre', 'numero', 'habilidad', 'tipo', ('apariencia', 'get_apariencia')
                
            ),
        }),
    )     

    def get_tipos(self, obj):
        return " - ".join([n.nombre for n in obj.tipo.all()])

    get_tipos.short_description = "Tipo"   

class LugarAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'get_foto')
    list_filter = ['nombre']
    search_fields = ['nombre']

    fieldsets = (
        (None, {
            "fields": ('nombre', ('foto', 'get_foto')
                
            ),
        }),
    )  

    readonly_fields = ('get_foto',)

class BatallaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'lugar','get_luchadores', 'ganador')
    list_filter = ('fecha', 'luchadores', 'ganador', 'lugar')
    filter_horizontal = ('luchadores',)
    search_fields = ['fecha', 'lugar__nombre', 'luchadores__nombre', 'ganador__nombre']

    def get_luchadores(self, obj):
        return " - ".join([n.nombre for n in obj.luchadores.all()])

    get_luchadores.short_description = "Luchadores"   

# Register your models here.

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Pokemon, PokemonAdmin,)
admin.site.register(Batalla, BatallaAdmin,)
admin.site.register(Lugar, LugarAdmin)
