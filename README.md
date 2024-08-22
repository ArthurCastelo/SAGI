

```markdown
# Lista de Produtos

Sistema web para gerenciar produtos com CRUD completo, utilizando Python e o framework Django, dbsqlite, e Bootstrap.

## Sumário

- [Sobre o Projeto](#sobre-o-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Configuração do E-mail](#configuração-do-e-mail)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Sobre o Projeto

O projeto **Lista de Produtos** é um sistema web desenvolvido para gerenciar produtos, permitindo a criação, leitura, atualização e exclusão (CRUD) de registros. O sistema foi construído utilizando Django, um framework de desenvolvimento web em Python, e estilizado com Bootstrap para um design responsivo e moderno. O banco de dados utilizado é o SQLite, que é leve e fácil de configurar.

## Tecnologias Utilizadas

- Python
- Django
- SQLite
- Bootstrap
- HTML/CSS
- JavaScript

## Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:

- [Git](https://git-scm.com)
- [Python](https://www.python.org/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

Além disto, é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/).

## Instalação

1. Clone este repositório:
   ```sh
   git clone https://github.com/ArthurCastelo/Lista-de-Produtos.git
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```

5. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Uso

1. Acesse o sistema no seu navegador:
   ```
   http://127.0.0.1:8000/
   ```

2. Utilize a interface para gerenciar produtos:
   - Crie novos produtos
   - Visualize a lista de produtos
   - Atualize informações de produtos existentes
   - Exclua produtos

## Configuração do E-mail

Para que a funcionalidade de redefinição de senha funcione corretamente, é necessário configurar o backend de e-mail no arquivo `settings.py` do seu projeto Django. Por padrão, o Django usa o backend de e-mail em memória, que não envia e-mails reais.

Para configurar o envio de e-mails, você pode usar um serviço de e-mail real. Aqui está um exemplo de configuração para usar o Gmail como backend de e-mail:

```python
# settings.py

# Configurações do backend de e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha'
```

Certifique-se de substituir `'seu-email@gmail.com'` e `'sua-senha'` pelos detalhes da sua conta de e-mail. Se você usar um serviço diferente, consulte a documentação do serviço para obter as configurações corretas.

## Contribuição

Contribuições são sempre bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para criar issues e pull requests.

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Faça o push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## Contato

Arthur Castelo - [arthurcastelo1205@gmail.com](mailto:arthurcastelo1205@gmail.com)

GitHub: [ArthurCastelo](https://github.com/ArthurCastelo)
```

Essa seção sobre a configuração do e-mail vai ajudar a garantir que os usuários do projeto possam configurar corretamente o envio de e-mails para funcionalidades como a redefinição de senha.
