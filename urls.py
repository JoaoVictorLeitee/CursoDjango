from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="receita-home"),
    path('receitas/<int:id>/', views.receita, name="receitas-receita"),
]
