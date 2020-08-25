from django.urls import path
from nations import views

app_name = 'nations'

urlpatterns = [
    path('biomes/', views.BiomeList.as_view(), name='biome-list'),
    path('regions/', views.RegionList.as_view(), name='region-list'),

    path('governments/', views.GovernmentList.as_view(), name='government-list'),

    path('buildings/', views.BuildingList.as_view(), name='building-list'),

    path('nations/', views.NationList.as_view(), name='nation-list'),
    path('nations/<int:pk>/', views.NationDetail.as_view(), name='nation-detail'),
    path('nations/<int:pk>/buildings/', views.NationBuildings.as_view(), name='nation-buildings'),
]