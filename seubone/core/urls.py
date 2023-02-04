from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('estoque/', views.estoque, name="estoque"),
]