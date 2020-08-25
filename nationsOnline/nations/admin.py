from django.contrib import admin
from nations import models

# Register your models here.
admin.site.register(models.Biome)
admin.site.register(models.BiomeBoost)

admin.site.register(models.Government)
admin.site.register(models.GovernmentBoost)

admin.site.register(models.TroopInfo)

admin.site.register(models.ResourceBuildingInfo)
admin.site.register(models.MilitaryBuildingInfo)

admin.site.register(models.Region)
admin.site.register(models.Nation)