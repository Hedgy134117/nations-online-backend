from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='register-user'),
]