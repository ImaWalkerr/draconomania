from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('base', views.base, name='base'),
    path('homes', views.homes, name='homes'),
    path('islands', views.islands, name='islands'),
    path('dragons_catalog', views.dragons_catalog, name='dragons_catalog'),
    path('draconomania_store', views.draconomania_store, name='draconomania_store'),
    path('resource_elements', views.resource_elements, name='resource_elements'),
    path('resource_symbols', views.resource_symbols, name='resource_symbols'),
    path('resource_food', views.resource_food, name='resource_food'),
    path('dragons', views.dragons, name='dragons'),
    path('translate', views.translate, name='translate'),
]
