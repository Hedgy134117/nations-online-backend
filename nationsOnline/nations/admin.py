from django.contrib import admin
from nations import models

# Register your models here.
admin.site.register(models.Biome)
admin.site.register(models.Region)
admin.site.register(models.Government)
admin.site.register(models.GovernmentBoost)