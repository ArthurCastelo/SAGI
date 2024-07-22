from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from mercado.views import cadastrar,listar_produtos,remover,editar,pesquisar,registrar,entrar,sair

urlpatterns = [
    path('',entrar, name='realizar_login'),
    path('sair/',sair, name="logout"),
    path('registrar/',registrar),
    path('cadastrar/',cadastrar, name='cadastrar_produto'),
    path('listar/',listar_produtos,name='listar_produtos'),
    path('remover/<int:id>',remover),
    path('editar/<int:id>',editar),
    path('pesquisar/',pesquisar),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]