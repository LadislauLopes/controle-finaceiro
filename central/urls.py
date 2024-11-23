from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_entrada', views.adicionar_entrada, name='adicionar_entrada'),  # Esse é o correto
]
