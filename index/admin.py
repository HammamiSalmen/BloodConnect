from django.contrib import admin
from .models import (
    Donneur,
    Hopital,
    DemandeUrgente,
    Don,
    Campagne,
    Inscription,
    ReponseAppel,
)


@admin.register(Donneur)
class DonneurAdmin(admin.ModelAdmin):
    list_display = ("user", "groupe_sanguin", "ville", "actif")
    list_filter = ("groupe_sanguin", "ville", "actif")


@admin.register(Hopital)
class HopitalAdmin(admin.ModelAdmin):
    list_display = ("nom", "ville", "agrement", "valide")
    list_filter = ("valide", "ville")
    search_fields = ("nom", "agrement")


@admin.register(DemandeUrgente)
class DemandeUrgenteAdmin(admin.ModelAdmin):
    list_display = ("hopital", "groupe_sanguin", "quantite", "statut", "delai")
    list_filter = ("statut", "groupe_sanguin")


admin.site.register(Don)
admin.site.register(Campagne)
admin.site.register(Inscription)
admin.site.register(ReponseAppel)
