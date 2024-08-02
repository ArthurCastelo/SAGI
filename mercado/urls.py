from django.urls import path
from mercado.views import (cadastrar, listar_produtos, remover, editar, pesquisar, registrar, entrar, sair, 
                           redefinir_senha, deletar_conta, enviar_email, confirmar_email)

urlpatterns = [
    path('', entrar, name='realizar_login'),
    path('sair/', sair, name="logout"),
    path('registrar/', registrar),
    path('cadastrar/', cadastrar, name='cadastrar_produto'),
    path('listar/', listar_produtos, name='listar_produtos'),
    path('remover/<int:id>', remover),
    path('deletar/<int:id>', deletar_conta, name='deletar_conta'),
    path('editar/<int:id>', editar),
    path('pesquisar/', pesquisar),
    path('redefinir_senha/<int:user_id>/', redefinir_senha, name="redefinir_senha"),
    path('confirmar_email/', confirmar_email, name="confirmar_email"),
    path('reset_password/', enviar_email, name="enviar_email_reset"),
]
