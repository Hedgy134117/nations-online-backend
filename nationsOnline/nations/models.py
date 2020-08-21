from django.db import models
import math

class Biome(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

class BiomeBoost(models.Model):
    choices = [
        ('food', 'Food'),
        ('iron', 'Iron'),
        ('aluminum', 'Aluminum'),
        ('steel', 'Steel'),
        ('wood', 'Wood'),
        ('rawUranium', 'Raw Uranium'),
        ('enrichedUranium', 'Enriched Uranium'),
        ('oil', 'Oil'),
    ]

    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    resource = models.CharField(max_length=100, choices=choices)
    percentage = models.FloatField()

class Region(models.Model):
    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Government(models.Model):
    name = models.CharField(max_length=100, default='')
    populationRate = models.FloatField()

    def __str__(self):
        return self.name

class GovernmentBoost(models.Model):
    choices = [
        ('construction', 'Construction'),
        ('research', 'Research'),
        ('happiness', 'Happiness'),
        ('crime', 'Crime'),
        ('military', 'Military'),
    ]

    government = models.ForeignKey('nations.Government', models.CASCADE)
    resource = models.CharField(max_length=100, choices=choices)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.government.name} {self.resource} {self.percentage * 100}%'

class Nation(models.Model):
    name = models.CharField(max_length=254)
    owner = models.ForeignKey('authentication.User', models.CASCADE, default='')
    region = models.ForeignKey('nations.Region', models.CASCADE)
    government = models.ForeignKey('nations.Government', models.CASCADE, default=1)
    population = models.FloatField(default=0)

    # Resources
    food = models.FloatField(default=0)
    iron = models.FloatField(default=0)
    aluminum = models.FloatField(default=0)
    steel = models.FloatField(default=0)
    wood = models.FloatField(default=0)
    rawUranium = models.FloatField(default=0)
    enrichedUranium = models.FloatField(default=0)
    oil = models.FloatField(default=0)

    # Other resources
    construction = models.FloatField(default=0)
    research = models.FloatField(default=0)
    happiness = models.FloatField(default=0)
    crime = models.FloatField(default=0)
    military = models.FloatField(default=0)

    def grow_population(self):
        self.population = self.population * math.exp(self.government.populationRate)

class ResourceBoost(models.Model):
    choices = [
        ('food', 'Food'),
        ('iron', 'Iron'),
        ('aluminum', 'Aluminum'),
        ('steel', 'Steel'),
        ('wood', 'Wood'),
        ('rawUranium', 'Raw Uranium'),
        ('enrichedUranium', 'Enriched Uranium'),
        ('oil', 'Oil'),
    ]

    nation = models.ForeignKey('nations.Nation', models.CASCADE)
    resource = models.CharField(max_length=100, choices=choices)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.nation.name} {self.resource} {self.percentage * 100}%'