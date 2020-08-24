from django.db import models
import math

resourceChoices = [
    ('food', 'Food'),
    ('iron', 'Iron'),
    ('aluminum', 'Aluminum'),
    ('steel', 'Steel'),
    ('wood', 'Wood'),
    ('rawUranium', 'Raw Uranium'),
    ('enrichedUranium', 'Enriched Uranium'),
    ('oil', 'Oil'),
]
boostChoices = [
    ('construction', 'Construction'),
    ('research', 'Research'),
    ('happiness', 'Happiness'),
    ('crime', 'Crime'),
    ('military', 'Military'),
]

# ---------- MAP ---------- # 

class Biome(models.Model):
    name = models.CharField(max_length=254)
    
    def __str__(self):
        return self.name

class BiomeBoost(models.Model):
    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    resource = models.CharField(max_length=100, choices=resourceChoices)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.biome.name} {self.resource} {self.percentage * 100}%'

class Region(models.Model):
    biome = models.ForeignKey('nations.Biome', models.CASCADE)
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

# ---------- GOVERNMENT ---------- # 

class Government(models.Model):
    name = models.CharField(max_length=100, default='')
    populationRate = models.FloatField()

    def __str__(self):
        return self.name

class GovernmentBoost(models.Model):
    government = models.ForeignKey('nations.Government', models.CASCADE)
    resource = models.CharField(max_length=100, choices=boostChoices)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.government.name} {self.resource} {self.percentage * 100}%'

# ---------- MILITARY ---------- #
class TroopInfo(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Troop(models.Model):
    info = models.ForeignKey('nations.TroopInfo', models.CASCADE)

# ---------- BUILDING ---------- #
 
class BuildingInfo(models.Model):
    name = models.CharField(max_length=254)
    desc = models.TextField()

    # Resources
    foodCost = models.IntegerField(default=0)
    ironCost = models.IntegerField(default=0)
    aluminumCost = models.IntegerField(default=0)
    steelCost = models.IntegerField(default=0)
    woodCost = models.IntegerField(default=0)
    rawUraniumCost = models.IntegerField(default=0)
    enrichedUraniumCost = models.IntegerField(default=0)
    oilCost = models.IntegerField(default=0)

    constructionTime = models.IntegerField(verbose_name='Construction Time (in hours)')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class ResourceBuildingInfo(BuildingInfo):
    resource = models.CharField(verbose_name='Producing Resource', max_length=254, choices=resourceChoices)
    rpc = models.IntegerField()

class MilitaryBuildingInfo(BuildingInfo):
    troop = models.ForeignKey('nations.TroopInfo', models.CASCADE)
    housing = models.IntegerField()

class Building(models.Model):
    nation = models.ForeignKey('nations.Nation', models.CASCADE)
    startedBuildingTime = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class ResourceBuilding(Building):
    info = models.ForeignKey('nations.ResourceBuildingInfo', models.CASCADE)
    lastLoad = models.DateTimeField(auto_now=True)

class MilitaryBuilding(Building):
    info = models.ForeignKey('nations.MilitaryBuildingInfo', models.CASCADE)

# ---------- NATION ---------- # 

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
    
    def __str__(self):
        return self.name

class ResourceBoost(models.Model):
    nation = models.ForeignKey('nations.Nation', models.CASCADE)
    resource = models.CharField(max_length=100, choices=resourceChoices)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.nation.name} {self.resource} {self.percentage * 100}%'