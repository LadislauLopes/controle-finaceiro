from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar_mov', views.adicionar_mov, name='adicionar_mov'), 
    path('adicionar_categoria', views.adicionar_categoria, name='adicionar_categoria'),  
    path('adicionar_pessoa', views.adicionar_pessoa, name='adicionar_pessoa'),  
    path('adicionar_conta', views.adicionar_conta, name='adicionar_conta'),  
]
