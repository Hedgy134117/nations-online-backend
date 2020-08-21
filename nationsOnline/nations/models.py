from django.db import models
import math

class Biome(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

class Region(models.Model):
    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Government(models.Model):
    name = models.CharField(max_length=100, default='')
    populationRate = models.FloatField()

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

class Nation(models.Model):
    name = models.CharField(max_length=254)
    owner = models.ForeignKey('authentication.User', models.CASCADE)
    region = models.ForeignKey('nations.Region', models.CASCADE)
    government = models.ForeignKey('nations.Government', models.CASCADE)
    population = models.FloatField()

    # Resources
    food = models.FloatField()
    iron = models.FloatField()
    aluminum = models.FloatField()
    steel = models.FloatField()
    wood = models.FloatField()
    rawUranium = models.FloatField()
    enrichedUranium = models.FloatField()
    oil = models.FloatField()

    # Other resources
    construction = models.FloatField()
    research = models.FloatField()
    happiness = models.FloatField()
    crime = models.FloatField()
    military = models.FloatField()

    def grow_population(self):
        self.population = self.population * math.exp(self.government.populationRate)