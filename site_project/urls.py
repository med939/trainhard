from django.urls import path
from . import views



urlpatterns = [
    path('',views.home, name = 'home'),
    path('Parfum_h', views.Parfum_h, name = 'Parfum homme'),
    path('Parfum_f', views.Parfum_f, name = 'Parfum femme'),
    path('Maquillage', views.Maquillage, name = 'Maquillage'),
    path('Produit/<str:pk>/', views.Produit, name = 'Produit'),
    path('Search', views.Search, name = 'Recherche'),
]