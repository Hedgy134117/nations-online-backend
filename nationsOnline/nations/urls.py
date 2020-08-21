from django.urls import path
from nations import views

urlpatterns = [
    path('biomes/', views.BiomeList.as_view(), name='biome-list'),
    
    path('regions/', views.RegionList.as_view(), name='region-list'),

    path('governments/', views.GovernmentList.as_view(), name='government-list'),

    path('nations/', views.NationList.as_view(), name='nation-list'),
]