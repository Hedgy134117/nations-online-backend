from django.db import models

# Create your models here.
class Biome(models.Model):
    name = models.CharField(max_length=254)

class Region(models.Model):
    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    name = models.CharField(max_length=254)