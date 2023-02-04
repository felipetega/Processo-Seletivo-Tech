from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('estoque/', views.estoque, name="estoque"),


    path('excluir/<str:id>', views.excluir, name="excluir"),
    path('alterar/<str:id>', views.alterar, name="alterar"),
    path('subtrair_estoque/<str:id>', views.subtrair_estoque, name="subtrair_estoque"),

    
]