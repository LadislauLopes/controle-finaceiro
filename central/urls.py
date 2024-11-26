from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_saida', views.adicionar_saida, name='adicionar_saida'), 
    path('adicionar_categoria', views.adicionar_categoria, name='adicionar_categoria'),  
    path('adicionar_pessoa', views.adicionar_pessoa, name='adicionar_pessoa'),  
]
