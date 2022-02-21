from django.contrib import admin
from .models import Tipo, Pokemon, Lugar, Batalla
from  django.contrib.auth.models  import  Group

admin.site.unregister(Group)

class TipoAdmin(admin.ModelAdmin):
    list_filter = ['nombre']
    search_fields = ['^nombre']

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'numero', 'habilidad', 'get_tipos', 'get_apariencia')
    list_filter = ('nombre', 'numero', 'tipo')
    search_fields = ['^nombre', '^numero', '^tipo__nombre']
    # filter_horizontal = ('tipo',)
    # ordering = ['nombre']
    autocomplete_fields = ['tipo']  
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
    search_fields = ['^nombre']
    readonly_fields = ('get_foto',)

    fieldsets = (
        (None, {
            "fields": ('nombre', ('foto', 'get_foto')
                
            ),
        }),
    )  

class BatallaAdmin(admin.ModelAdmin):
    list_display = ('fecha','get_luchadores', 'ganador', 'lugar', 'get_lugar')
    list_filter = ('fecha', 'luchadores', 'ganador', 'lugar')
    filter_horizontal = ('luchadores',)
    search_fields = ['fecha', '^lugar__nombre', '^luchadores__nombre', '^ganador__nombre']
    autocomplete_fields = ['luchadores', 'ganador', 'lugar']

    def get_luchadores(self, obj):
        return " - ".join([n.nombre for n in obj.luchadores.all()])

    get_luchadores.short_description = "Luchadores"

    def get_lugar(self, obj):
        return obj.lugar.get_foto()

    get_lugar.short_description = "Imagen Lugar"   

admin.site.register(Tipo, TipoAdmin)
admin.site.register(Pokemon, PokemonAdmin,)
admin.site.register(Batalla, BatallaAdmin,)
admin.site.register(Lugar, LugarAdmin)
