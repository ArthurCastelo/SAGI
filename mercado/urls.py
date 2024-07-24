from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from mercado.views import cadastrar,listar_produtos,remover,editar,pesquisar,registrar,entrar,sair,redefinir_senha

urlpatterns = [
    path('',entrar, name='realizar_login'),
    path('sair/',sair, name="logout"),
    path('registrar/',registrar),
    path('cadastrar/',cadastrar, name='cadastrar_produto'),
    path('listar/',listar_produtos, name='listar_produtos'),
    path('remover/<int:id>',remover),
    path('editar/<int:id>',editar),
    path('pesquisar/',pesquisar),
    path('redefinir_senha/',redefinir_senha, name="redefinir_senha")
]