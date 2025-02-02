from django.shortcuts import render, redirect,get_object_or_404
from .models import Produtos
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse


def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)

@require_http_methods(["GET", "POST"])
def registrar(request):
    if request.method == 'POST':
            email = request.POST.get('email')
            username= request.POST.get('username')

            if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
                return redirect('/registrar/?cd_erro=2&error=Já existe uma conta com esse nome ou e-mail!')
            else:
                username = request.POST.get('username')
                email = request.POST.get('email')
                senha = request.POST.get('senha')

                novoUsuario = User.objects.create_user(username=username, email=email, password=senha)
                novoUsuario.save()

                # Visualizar a página de login
                return redirect('/?code_success=10')
                
        
    #CASO HAJA ALGUM ERRO, DADOS PASSADOS VIA GET
    cd_erro = request.GET.get('cd_erro')
    error = request.GET.get('error')

    return render(request, 'index.html',{'cd_erro':cd_erro,'error':error})

@require_http_methods(["GET", "POST"])
def entrar(request):
    if request.method == 'POST':
        try:
            usuario_aux = User.objects.get(email=request.POST['email'])
            usuario = authenticate(username=usuario_aux.username,
                                   password=request.POST["senha"])
            if usuario is not None:
                login(request, usuario)
                return HttpResponseRedirect('listar/')
            else:
                return redirect('/?cd_erro=3&error=Dados inválidos!')
        except User.DoesNotExist:
            return redirect('/?cd_erro=3&error=Usuário não encontrado!')

    code_success = request.GET.get('code_success')
    cd_erro = request.GET.get('cd_erro')
    error = request.GET.get('error')
    return render(request, 'login.html', {'cd_erro': cd_erro, 'error': error, 'code_success': code_success})


@login_required
def sair(request):
    logout(request)
    return render(request,'login.html')

def cadastrar(request):
    if request.method == 'GET':
        cd_erro = request.GET.get('cd_erro')
        error = request.GET.get('error')
        return render(request, 'cadastrar.html',{'cd_erro':cd_erro,'error':error})
    elif request.method == 'POST':
        # Armazenando os dados via POST vindo do formulário
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')

        if len(nome) <=0 or len(valor) <=0:
            return redirect('/cadastrar/?cd_erro=1&error=Dados inválidos, digite valores nos campos!')

        # Criando um objeto Produtos e enviando para o banco de dados
        produto = Produtos(nome=nome, valor=valor)
        produto.save()
        return redirect('/listar/?code_success=11')

def listar_produtos(request):
    code_success = request.GET.get('code_success')

    #para pegar qual id é o do usuário
    user_id = request.user.id
    todos_produtos = Produtos.objects.all()
    usuario_atual = request.user  # Usuário atual logado
    return render(request,'listar_produtos.html',{'todos_produtos':todos_produtos, 'code_success':code_success, 'user_id':user_id, 'usuario_atual':usuario_atual})

def confirmar_email(request):
   return render(request,'reset_password.html')

def enviar_email(request):
    if request.method == 'POST':
        assunto = 'Redefinir Senha - SAGI'
        remetente = 'fusion.iom@hotmail.com'
        destinatario = request.POST.get('email_redefinir')

        try:
            usuario = User.objects.get(email=destinatario)
            mensagem = f'Olá, acesse o link para redefinir a sua senha: http://127.0.0.1:8000/redefinir_senha/{usuario.id}'
            
            send_mail(
                assunto,
                mensagem,
                remetente,
                [destinatario],  
                fail_silently=False,
            )
            
            return redirect('/reset_password/?code_success=500')
        except User.DoesNotExist:
            return render(request, 'reset_password.html', {'error': 'Email não encontrado'})

    code_success = request.GET.get('code_success')
    error = request.GET.get('error')
    return render(request, 'reset_password.html', {'code_success': code_success, 'error': error})
   


def pesquisar(request):
    nome_filtrar = request.GET.get('nome_filtrar')
    if nome_filtrar:
        todos_produtos = Produtos.objects.filter(nome__icontains=nome_filtrar)
    else:
        todos_produtos = Produtos.objects.all()
    return render(request,'listar_produtos.html',{'todos_produtos':todos_produtos})

def remover(request,id):
    id_remover = Produtos.objects.get(id=id)
    id_remover.delete()
    return redirect('/listar/')

def editar(request, id):
    produto = get_object_or_404(Produtos, id=id)

    if request.method == 'POST':
        nome = request.POST.get('nome')
        valor = request.POST.get('valor')
        produto.nome = nome
        produto.valor = valor
        produto.save()
        return redirect('/listar/')
    else:
        return render(request, 'editar_produto.html', {'produto': produto})

@require_http_methods(["GET", "POST"])
def redefinir_senha(request, user_id=None):
    user = get_object_or_404(User, pk=user_id) if user_id else request.user
    
    if request.method == 'POST':
        new_password = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if new_password != new_password2:
            return redirect(f'/redefinir_senha/{user.id}/?cd_error=30')
        elif user.check_password(new_password):
            return redirect(f'/redefinir_senha/{user.id}/?cd_error=40')
        else:
            user.set_password(new_password)
            user.save()
            return redirect('/?code_success=100')

    cd_error = request.GET.get('cd_error')
    return render(request, 'redefinir_senha.html', {'cd_error': cd_error, 'user_id': user.id})

@login_required
def deletar_conta(request, id):
    id_user = get_object_or_404(User, id=id)
    id_user.delete()
    return render(request,'conta_excluida.html')





    

        



    